'''
setup.py is the build script for a Python project. It tells setuptools (Python’s package manager) how to install your project and its dependencies.
'''
from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str) -> List[str]:
    # This function will return a list of requirements
    HYPEN_E_DOT = "-e ."
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # removing the /n by using replace function with blank
        requirements = [req.replace("\n", "") for req in requirements]
        # if -e . is present in the requirements then remove it
        if HYPEN_E_DOT in requirements:
           requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name="mlproject", 
    version="0.0.1",
    author="Akash Vishwakarma",
    author_email="vishwakarmaakashav17@gmail.com",
    packages=find_packages(),
    # get_requirements function to read requirements from a file requirements.txt
    # and return a list of requirements
    install_requires=get_requirements("requirements.txt"),
)