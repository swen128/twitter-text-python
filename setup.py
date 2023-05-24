from setuptools import setup, find_packages

with open("README.rst", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="twitter-text-parser",
    version="2.0.1",
    author="swen128",
    author_email="fujjisaaan@gmail.com",
    description="A library to parse or validate Twitter texts properly",
    long_description=long_description,
    url="https://github.com/swen128/twitter-text-python",
    packages=find_packages(),
    install_requires=[
        "attrs>=19.3.0"
    ],
    python_requires='~=3.6',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Text Processing"
    ],
    package_data={
        'twitter_text.regexp': ['*.txt']
    }
)
