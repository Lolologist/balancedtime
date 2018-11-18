from setuptools import setup
from setuptools import find_packages
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.rst"), "r") as fh:
    long_description = fh.read()

setup(
    name='balanced-time',
    version='0.106',
    author="Daniel Bishop",
    author_email="lolologist@gmail.com",
    description="Convert regular time into 12-hour days and nights",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url='https://github.com/Lolologist/balanced_time',
    py_modules=["balanced_time"],
    install_requires=['astral','uszipcode'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ]
)
