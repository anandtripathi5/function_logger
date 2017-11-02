from setuptools import setup

version = '0.1'

setup(name='function_logger',
      version=version,
      description="logs the function functionality",
      long_description="""decorator that takes the logger and logs the request
       parameter with the function name and logs the return parameter
       of function""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Anand Tripathi',
      author_email='anand.tripathi507@gmail.com',
      url='https://github.com/anandtripathi5/function_logger',
      packages=['function_logger'],
      )