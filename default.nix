{
  self,
  lib,
  pyproject,
  buildPythonPackage,
  setuptools,
  pytestCheckHook,
  isodate,
  httpx,
  loguru,
  xsdata-pydantic,
}:
buildPythonPackage {
  pname = pyproject.project.name;
  version = pyproject.project.version;
  pyproject = true;

  src = self;

  build-system = [ setuptools ];

  dependencies = [
    httpx
    loguru
    xsdata-pydantic
    isodate
  ];

  nativeCheckInputs = [ pytestCheckHook ];

  pythonImportsCheck = [
    "entsoe"
  ];

  meta = {
    description = "Python Package to Query the ENTSO-E API";
    homepage = "https://github.com/berrij/entsoe-apy";
    license = lib.licenses.gpl3Only;
    maintainers = with lib.maintainers; [ berrij ];
    platforms = lib.platforms.all;
  };
}
