from setuptools import setup
from setuptools import find_packages
setup(
    name='balanced_time',
    version='0.101',
    scripts=['balanced_time.py'],
    author="Daniel Bishop",
    author_email="lolologist@gmail.com",
    description="Convert regular time into 12-hour days and nights",
    url='https://github.com/Lolologist/balanced-time',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ]
)
