import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="ihela-oauth2-provider",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    license="BSD License",  # example license
    description="A simple Django app to enable oAuth2 for iHela with django-allauth.",
    long_description=README,
    url="https://ihela.online/",
    author="UbuViz",
    author_email="info@ubuviz.com",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.0",  # replace "X.Y" as appropriate
        "Framework :: Django :: 2.1",  # replace "X.Y" as appropriate
        "Framework :: Django :: 2.2",  # replace "X.Y" as appropriate
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",  # example license
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
