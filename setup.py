# coding: utf-8

"""
   Python SDK for OpenFGA

   API version: 0.1
   Website: https://openfga.dev
   Documentation: https://openfga.dev/docs
   Support: https://discord.gg/8naAwJfWN6
   License: [Apache-2.0](https://github.com/openfga/python-sdk/blob/main/LICENSE)

   NOTE: This file was auto generated by OpenAPI Generator (https://openapi-generator.tech). DO NOT EDIT.
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "openfga-sdk"
VERSION = "0.4.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.25.11", "six >= 1.16", "python-dateutil >= 2.8.2"]
REQUIRES.append("aiohttp >= 3.9.1")

from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name=NAME,
    version=VERSION,
    description="A high performance and flexible authorization/permission engine built for developers and inspired by Google Zanzibar.",
    author="OpenFGA (https://openfga.dev)",
    author_email="community@openfga.dev",
    url="https://github.com/openfga/python-sdk",
    classifiers=[
      'Development Status :: 5 - Production/Stable',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: Apache Software License',
      'Programming Language :: Python :: 3.10',
      'Programming Language :: Python :: 3.11',
      'Programming Language :: Python :: 3.12',
    ],
    keywords=["openfga", "authorization", "fga", "fine-grained-authorization", "rebac", "zanzibar"],
    install_requires=REQUIRES,
    python_requires='>=3.10',
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache-2.0",
    long_description_content_type='text/markdown',
    long_description=long_description
)
