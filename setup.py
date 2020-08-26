#!/usr/bin/env python
import os
from setuptools import setup


def read(fname):
    """ Reads a file in from disk and returns its contents """
    with open(os.path.join(os.path.dirname(__file__), fname), "r") as file_handle:
        return file_handle.read()


setup(
    name="gmic-sphinx",
    version="0.0.1",
    author="Jonathan-David Schröder",
    author_email="jonathan.schroder@gmail.com",
    description=(
        "A simple sphinx extension to generate images from G'MIC commands"
    ),
    keywords="sphinx extension gmic image-processing",
    url="https://github.com/myselfhimself/gmic-sphinx",
    long_description=read("README.md"),
    packages=["gmic_sphinx"],
    include_package_data=True,
    install_requires=["sphinx", "docutils", "gmic"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: CEA CNRS Inria Logiciel Libre License, version 2.1 (CeCILL-2.1)",
        "Programming Language :: Python",
        "Topic :: Utilities",
    ],
)

