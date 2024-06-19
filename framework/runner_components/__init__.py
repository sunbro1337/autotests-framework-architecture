# modules
from . import main

# subpackages
from . import artifacts_manager, environment_manager, logger


# __all__ = ["function1", "function2", "Class1", "Class2"] with imported functions and class from module
# or for entire module __all__ = ["module1"] without any import from the module
__all__ = [
    # modules
    "main",

    # subpackages
    "artifacts_manager",
    "environment_manager",
    "logger"
]
__version__ = "0.0.0"


def initialize_package():
    print(f"Package {__name__} v{__version__} initialized")


initialize_package()
