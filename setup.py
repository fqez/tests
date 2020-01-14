from setuptools import setup, find_packages

import os
thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'
install_requires = [] # Examples: ["gunicorn", "docutils>=0.3", "lxml==0.5a7"]
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()
        
MAJOR               = 0
MINOR               = 2
MICRO               = 0
ISRELEASED          = False
VERSION             = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

setup(name='testsfqez',
      version=VERSION,
      description="mysetup",
      url="https://github.com/fqez/tests",
      packages=find_packages(exclude='test'),
      include_package_data=True,
      install_requires=install_requires,
      zip_safe=True)
