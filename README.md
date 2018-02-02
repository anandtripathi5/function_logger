# function_logger
Pip install-able library that logs the function functionality in log file. Function logger is a decorator that logs the function name and function argument when function is called and return parameters of functions when function is ended



Installation Instruction!
===================

>- Activate your Virtual Environment.
>- pip install function-logger

----------

**function-logger** is library having function logger that logs the function parameters.

# Features

 1. Function logger library comes with a function_logger decorator that takes a logger and logs the request paramters with function name and logs the return of function.

# Usage

 1. Import function logger library
	 -  `from function_logger import function_logger`

# Example

```python
from function_logger import function_logger
from logger import logger
# logger of your project

@function_logger(logger)
def log_function(name=None, age=None):
    logger.debug("Inside log function")
    return dict(bmi=19)


if __name__ == "__main__":
	bmi = log_function(name="hello", age=13)
	print bmi
```
