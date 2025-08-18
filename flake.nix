{
  description = "Rolch Development Shell";

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
      r_httpgd = pkgs.rPackages.buildRPackage {
        name = "httpgd";
        src = pkgs.fetchFromGitHub {
          owner = "nx10";
          repo = "httpgd";
          rev = "v2.0.4";
          sha256 = "vs6MTdVJXhTdzPXKqQR+qu1KbhF+vfyzZXIrFsuKMtU=";
        };
        propagatedBuildInputs = with pkgs.rPackages; [
          unigd
          AsioHeaders
        ];
      };
    in
    {
      devShells.${system}.default = pkgs.mkShell rec {
        name = "Python";
        venvDir = "./.venv";
        buildInputs = [
          # Keep these for some CUDA magic
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
          pypkgs.xsdata

          # Must have
          pkgs.R
          pkgs.radian
          pkgs.rPackages.languageserver
          pkgs.rPackages.lintr
          pkgs.rPackages.styler
          r_httpgd
          pkgs.rPackages.crayon
          pkgs.rPackages.cli

          # Project specific
          pkgs.rPackages.tidyverse
          pkgs.rPackages.tictoc
          pkgs.rPackages.dbx
          pkgs.rPackages.RMySQL

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
          mkdir -p .bin
          ln -sf ${pkgs.radian}/bin/radian .bin/
          # allow pip to install wheels
          unset SOURCE_DATE_EPOCH
        '';
      };
    };
}
