#!/usr/bin/env python3
# This file is part of phishdetect-python:
# https://github.com/phishdetect/phishdetect-python
# See the file 'LICENSE' for copying permission.

import os
from setuptools import setup, find_packages

from phishdetect import __version__, __package_name__

description = "This is a Python3 library to easily interact with a PhishDetect Node API server"
# this_directory = os.path.abspath(os.path.dirname(__file__))
# with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as handle:
#     long_description = handle.read()

requires = (
    "requests",
)

def get_package_data(package):
    walk = [(dirpath.replace(package + os.sep, "", 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, "__init__.py"))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}

setup(
    name=__package_name__,
    version=__version__,
    author="Claudio Guarnieri",
    author_email="nex@nex.sx",
    description=description,
    long_description=description,
    install_requires=requires,
    packages=find_packages(),
    package_data=get_package_data("phishdetect"),
    include_package_data=True,
    keywords="security phishing phishdetect",
    license="MIT",
    classifiers=[
    ],
)
