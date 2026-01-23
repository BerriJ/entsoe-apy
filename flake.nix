{
  description = "ENTSO-E-apy Development Shell";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  };

  outputs =
    { self, nixpkgs }:
    let
      system = "x86_64-linux"; # Adjust if necessary
      pkgs = import nixpkgs {
        inherit system;
      };
      pyproject = fromTOML (builtins.readFile ./pyproject.toml);
    in
    {
      packages.${system} = rec {
        default = pkgs.python3.pkgs.callPackage (./default.nix) {
          self = self;
          lib = pkgs.lib;
          pyproject = pyproject;
        };
        entsoe-apy = default;
      };

      devShells.${system}.default = pkgs.mkShell {
        name = "Python";
        venvDir = "./.venv";
        buildInputs =
          with pkgs.python3.pkgs;
          [
            # Stuff needed for technical reasons
            ipykernel
            jupyterlab
            pyzmq # Adding pyzmq explicitly
            pip
            notebook
            jupyter
            jupyter-client
            venvShellHook
            ruff

            # Project specific
            numpy
            pandas
            mkdocs-material
            mkdocstrings
            mkdocstrings-python
            pytest
            build
            twine

          ]
          ++ [ pkgs.mkdocs ];

        env = {
          NIX_LD = nixpkgs.lib.fileContents "${pkgs.stdenv.cc}/nix-support/dynamic-linker";
          LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath (
            with pkgs;
            [
              stdenv.cc.cc
              stdenv.cc.cc.lib
            ]
          );
          EXTRA_CCFLAGS = "-I/usr/include";
        };

        # Run this command only after creating the virtual environment
        postVenvCreation = ''
          unset SOURCE_DATE_EPOCH
          pip install -r requirements.txt
        '';

        # This is optional and can be left out to run pip manually.
        postShellHook = ''
          if [ -f .env ]; then
            # Export variables from .env into the environment
            set -a
            source .env
            set +a
          fi
        '';
      };
    };
}
