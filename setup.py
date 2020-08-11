#!/usr/bin/env python3
# This file is part of phishdetect-python:
# https://github.com/phishdetect/phishdetect-python
# See the file 'LICENSE' for copying permission.

import os
from setuptools import setup, find_packages

__package_name__ = "phishdetect"
__version__ = "1.6"
__description__ = "This is a Python3 library and CLI tool " \
    "to easily interact with a PhishDetect Node API server"

requires = (
    "click",
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
    description=__description__,
    long_description=__description__,
    install_requires=requires,
    packages=find_packages(),
    package_data=get_package_data("phishdetect"),
    scripts=["bin/phishdetect-cli",],
    include_package_data=True,
    keywords="security phishing phishdetect",
    license="MIT",
    classifiers=[
    ],
)
