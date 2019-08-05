#!/usr/bin/env python

from setuptools import setup, find_packages

version = '0.1.0'

install_requires = []

with open('requirements.txt', 'r') as fh:
    for line in fh.readlines():
        if line.strip() and not line.strip().startswith('#'):
            install_requires.append(line.strip('\n'))

setup(
    name='pykit',
    version=version,
    description='A collection of python toolkit',
    long_description=open('README.md').read(),
    author='Fay Cheng',
    author_email='fay.cheng.cn@gmail.com',
    url='https://gihub.com/faycheng/pykit',
    install_requires=install_requires,
    license='MIT',
    packages=find_packages(),
    py_modules=['cli'],
    entry_points={
        'console_scripts': ['i18n=cli:cli']},
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)