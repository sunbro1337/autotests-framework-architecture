# modules
from . import main

# subpackages
from . import checks, data_generator, steps, tests


# __all__ = ["function1", "function2", "Class1", "Class2"] with imported functions and class from module
# or for entire module __all__ = ["module1"] without any import from the module
__all__ = [
    # modules
    "main",

    # subpackages
    "checks",
    "data_generator",
    "steps",
    "tests"
]
__version__ = "0.0.0"


def initialize_package():
    print(f"Package {__name__} v{__version__} initialized")


initialize_package()
