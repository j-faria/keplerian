#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

# from setuptools import setup, find_packages
from setuptools import find_packages
from numpy.distutils.core import setup
from numpy.distutils.core import Extension

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [ ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

ext1 = Extension(name = 'keplerian.danby1988',
                 sources = ['extensions/danby1988.f90'],
                 extra_f90_compile_args=["-O3"])
ext2 = Extension(name = 'keplerian.true_anomaly',
                 sources = ['extensions/true_anomaly.f90'],
                 extra_f90_compile_args=["-O3"])
ext3 = Extension(name = 'keplerian.sincos',
                 sources = ['extensions/sincos.cpp'],
                 language='c++')

setup(
    author="João Faria",
    author_email='joao.faria@astro.up.pt',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Astronomers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="A package to calculate the Keplerian function",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='keplerian',
    name='keplerian',
    packages=find_packages(include=['keplerian']),
    ext_modules = [ext1, ext2, ext3],
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/j-faria/keplerian',
    version='0.1.0',
    zip_safe=False,
)
