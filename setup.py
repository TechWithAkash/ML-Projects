"""
setup.py is the build script for the ML project. It uses setuptools to handle
packaging, dependencies, and installation.
"""

from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements.txt file and returns a list of packages,
    excluding editable install marker '-e .'.
    """
    HYPEN_E_DOT = "-e ."
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Akash Vishwakarma",
    author_email="vishwakarmaakashav17@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
