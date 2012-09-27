#!/usr/bin/env python

import os.path
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='django-cms-aloha',
      version='0.0.1',
      description='django cms plugin to integrate the aloha editor',
      long_description=read('README'),
      author='Barry Rowlingson',
      author_email='b.rowlingson@gmail.com',
      url='https://github.com/spacedman/django-cms-aloha',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          ],
     )
