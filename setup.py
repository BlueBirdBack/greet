"""Setup script for the greet package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="greet",  # Replace with your desired package name
    version="0.1.0",
    author="Avery",
    author_email="avery@bluebirdback.com",
    description="A simple greeting library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BlueBirdBack/greet",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
