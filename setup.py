from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="twitter-text",
    version="0.0.1",
    author="swen128",
    author_email="fujjisaaan@gmail.com",
    description="Twitter Text Libraries for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/swen128/twitter-text-python",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Text Processing"
    ]
)
