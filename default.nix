with import <nixpkgs> {};
stdenv.mkDerivation rec {
  name = "env";

  # Mandatory boilerplate for buildable env
  env = buildEnv { name = name; paths = buildInputs; };
  builder = builtins.toFile "builder.sh" ''
    source $stdenv/setup; ln -s $env $out
  '';

  # Customizable development requirements
  buildInputs = [
    # Add packages from nix-env -qaP | grep -i needle queries
    # With Python configuration requiring a special wrapper
    postgresql_10
    #zlib
    #zlib.dev
    #python37Packages.pillow
    (python37.buildEnv.override {
      ignoreCollisions = true;
      extraLibs = with python37Packages; [
        # Add pythonPackages without the prefix
        pip
        django_2_2
        djangorestframework
        djangorestframework-jwt
        psycopg2
        django-cors-headers
        pillow
      ];
    })
  ];

  # Customizable development shell setup with at last SSL certs set
  #shellHook = ''
    #export SSL_CERT_FILE=${cacert}/etc/ssl/certs/ca-bundle.crt
  #'';
}
