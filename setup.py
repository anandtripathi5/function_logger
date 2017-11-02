from setuptools import setup, find_packages
import sys, os

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
      url='https://git.txtbox.in:8080/smcore/sm_utils',
      packages=['function_logger'],
      license='',
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
