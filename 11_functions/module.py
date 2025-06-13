import mymodule
print(mymodule.sum(124, 279))
import math
print(math.sqrt(16))  # This will print 4.0, the square root of 16
import os
#os.abort()  # This will raise an OSError, as it is used to abort the program
#Types of modules:
# 1. Built-in modules: These are modules that come with Python, such as `math`, `os`, and `sys`.    
# 2. External modules: These are modules that are not included with Python by default but can be installed separately, such as `numpy`, `pandas`, and `requests`.
# 3. Custom modules: These are modules that you create yourself, like `mymodule.py` in this example.    
# 4. Standard library modules: These are modules that are part of the Python standard library, such as `datetime`, `json`, and `re`.
# 5. Third-party modules: These are modules created by the Python community and can be installed using package managers like `pip`, such as `flask`, `django`, and `beautifulsoup4`.
# 6. Package modules: These are modules that are organized into packages, which are directories containing multiple modules. For example, `numpy` is a package that contains multiple modules for numerical computing.

import mymodule as mm  # Importing the module with an alias
print(mm.multiply(5, 6))  # This will print 30, the product of 5 and 6
print(mm.hello())  # This will print "Hello from mymodule!"
# Importing specific functions from a module