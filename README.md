# Guidelines

## Structure principle

```
root/
├── README.md
├── .gitignore
├── requirements.txt
├── setup_environment.py
├── module_name.py
├── framework_name/
│   ├── __init__.py
│   ├── module_name.py
│   └── package_name/
│       ├── __init__.py
│       ├── module_name.py
│       └── subpackage_name/
│           ├── __init__.py
│           └── module_name.py
```

- Naming follows pep8
- Modules and other files can be grouped in a directory
- Any non-git files and directories should be added to .gitignore

## Packages & subpackages

`__init__.py` of packages and subpackages should contain:
```python
# modules
from . import module_1, module_2, ... module_n

# subpackages
from . import subpackage_1, subpackage_2, ... subpackage_n


# __all__ = ["function1", "function2", "Class1", "Class2"] with imported functions and class from module
# or for entire module __all__ = ["module1"] without any import from the module
__all__ = [
    # modules
    "module_1", 
    "module_2", 
    ...
    "module_n"

    # subpackages
    "subpackage_1", 
    "subpackage_2",
    ... 
    "subpackage_n"
]
__version__ = "0.0.0"
```

## Dependencies & requirements

If possible ALL new dependencies(package, libs etc.) should be added to requirements.txt, otherwise it should be added to setup_environment.py

## Code style

### Import pattern

```python
# external libs & packages
import asyncio
import re
# from playwright.async_api import Playwright, async_playwright, expect, Page
from playwright.sync_api import Playwright, sync_playwright, expect, Page

# internal libs & packages
from .page_components import BaseComponent
```




