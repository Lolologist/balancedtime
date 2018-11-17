from setuptools import setup
setup(
    name='balanced-time',
    version='0.1',
    scripts=['balanced_time']
    author="Daniel Bishop",
    author_email="lolologist@gmail.com",
    description="Convert regular time into 12-hour days and nights",
    url='https://github.com/Lolologist/balanced-time'
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ]
)
