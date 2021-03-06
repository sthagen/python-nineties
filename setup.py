import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="nineties",
    version="0.0.5",
    description="Ease the reading of relics from the Nineties",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/sthagen/python-nineties",
    author="Stefan Hagen",
    author_email="stefan@hagen.link",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "nineties=nineties.cli:main",
        ]
    },
)
