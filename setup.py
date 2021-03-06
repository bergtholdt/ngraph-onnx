#!/usr/bin/env python

from distutils.core import setup

from setuptools import find_packages

setup(name='ngraph-onnx',
      version='0.2.0',
      description='ONNX support for ngraph',
      author='Intel',
      author_email='intelnervana@intel.com',
      url='http://www.intelnervana.com',
      license='License :: OSI Approved :: Apache Software License',
      packages=find_packages(exclude=['tests']),
      install_requires=['setuptools', 'numpy', 'onnx'])
