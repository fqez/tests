from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call


class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        develop.run(self)

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        check_call('python -m spacy download en').split()
        check_call('python -m spacy download es').split()
        install.run(self)

import os
thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'
install_requires = [] # Examples: ["gunicorn", "docutils>=0.3", "lxml==0.5a7"]
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()
        
MAJOR               = 0
MINOR               = 1
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
      cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
      },
      zip_safe=True)
