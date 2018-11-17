from setuptools import setup
from setuptools import find_packages
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "docs/source/index.rst"), "r") as fh:
    long_description = fh.read()

setup(
    name='balanced_time',
    version='0.103',
    scripts=['balanced_time.py'],
    author="Daniel Bishop",
    author_email="lolologist@gmail.com",
    description="Convert regular time into 12-hour days and nights",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url='https://github.com/Lolologist/balanced_time',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ]
)
