"""Script for setuptools."""

import glob
from setuptools import setup, find_packages


with open("README.md") as readme:
    long_description = readme.read()

version = "0.0.1"

deps = [
    "Pillow>=4.3.0",
    "psutil>=5.4.2",
    "colored>=1.3.93",
    "pygtrie>=2.3.3",
    "re-wx>=0.0.9",
    "typing-extensions==3.10.0.2",
    "wxpython>=4.1.0",
    'dataclasses>=0.8; python_version < "3.7"',
]

setup(
    name="GooeyEx",
    version=version,
    url="http://pypi.python.org/pypi/GooeyEx/",
    author="greats3an",
    author_email="greats3an@gmail.com",
    description=(
        "GooeyEx is a fork of Gooey, a Python library that turns command line programs into GUI applications."
    ),
    license="MIT",
    python_requires=">=3.6",
    packages=find_packages(),
    install_requires=deps,
    include_package_data=True,
    dependency_links=["http://www.wxpython.org/download.php"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Desktop Environment",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Widget Sets",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    long_description_content_type="text/markdown",
    long_description=long_description,
    data_files=glob.glob("GooeyEx/languages/*") + glob.glob("GooeyEx/images/*"),
)
