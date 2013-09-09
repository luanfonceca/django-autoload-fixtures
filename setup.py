#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup

try:
    long_description = file('README.rst').read()
except IOError:
    long_description = ''

setup(
    name='django-autoload-fixtures',
    version='0.2',
    url='https://github.com/luanfonceca/django-autoload-fixtures',
    license='BSD',
    description='This library allows you to load initial Fixtures automagically after the South migrate your Model.',
    long_description=long_description,
    author='Luan Fonseca',
    author_email='luanfonceca@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    packages=[
        'autoload_fixtures',
    ],
    install_requires=[
        'setuptools',
        'Django>=1.3',
        'south',
    ],
)