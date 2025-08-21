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
      pypkgs = pkgs.python313Packages;
    in
    {
      devShells.${system}.default = pkgs.mkShell rec {
        name = "Python";
        venvDir = "./.venv";
        buildInputs = [
          # Stuff needed for technical reasons
          pypkgs.ipykernel
          pypkgs.jupyterlab
          pypkgs.pyzmq # Adding pyzmq explicitly
          pypkgs.pip
          pypkgs.notebook
          pypkgs.jupyter
          pypkgs.jupyter-client
          pypkgs.venvShellHook
          pypkgs.ruff

          # Project specific
          pypkgs.numpy
          pypkgs.pandas
          pkgs.mkdocs
          pypkgs.mkdocs-material
          pypkgs.mkdocstrings
          pypkgs.mkdocstrings-python
          pypkgs.pytest

        ];

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
