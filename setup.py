#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='django-autoload-fixtures',
    version='0.1',
    url='https://github.com/luanfonceca/django-autoload-fixtures',
    license='BSD',
    description='This library allows you to load initial Fixtures automagically after the South migrate your Model.',
    long_description=file('README.md').read(),
    author='Luan Fonseca',
    author_email='luanfonceca@gmail.com',
    classifiers=[
        'Development Status :: 0 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
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
    # test_suite='runtests.runtests',
)