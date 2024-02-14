# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='replay',
    version='0.1.0',
    description='Replay package for Python-Guide.org',
    long_description=readme,
    author='Michael Daloia',
    author_email='donzeno23@yahoo.com',
    url='https://github.com/donzeno23/pyreplay',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
