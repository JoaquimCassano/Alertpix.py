#!/usr/bin/python
# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

requirements = [
    "qrcode",
    "requests"
]

setuptools.setup(
    name="alertpix",
    version="0.1",
    author="Joaquim Cassano",
    license='MIT',
    author_email="joaquim@cassano.com.br",
    description='Python library for communication with the alertpix api',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    keywords=["api", "alertpix", "payments", "pix"],
    url="https://github.com/JoaquimCassano/Alertpix.py",
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)