#!/usr/bin/env python3
import logging
import os

import setuptools

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(os.environ.get("LOG_LEVEL", "INFO"))

# Package meta-data.
NAME = "edr-pydantic-classes"
VERSION = "0.0.15"

feature_suffix = os.environ.get("FEATURE_SUFFIX", "")
logger.debug(f"Feature suffix: {feature_suffix}")

if feature_suffix:
    # Development branches should have a .devN suffix according to PEP-0440
    # See https://peps.python.org/pep-0440/#developmental-releases
    # TODO: This will clash with multiple branches working at the same time!
    VERSION += f".dev0+{feature_suffix}"
logger.debug(f"Package version: {VERSION}")

setuptools.setup(
    name=NAME,
    version=VERSION,
    author="KNMI Data Platform",
    author_email="dataplatform@knmi.nl",
    url="https://gitlab.com/KNMI/data-platform/observation-api/internal-data-api",
    description="The Pydantic models for EDR datatypes",
    package_data={"edr_pydantic_classes": ["py.typed"]},
    packages=["edr_pydantic_classes"],
    include_package_data=False,
    license="MIT",
    install_requires=[
        "pydantic~=2.3",
        "python-dateutil",
        "covjson-pydantic~=0.2.0",
    ],
    python_requires=">=3.10.0",
)
