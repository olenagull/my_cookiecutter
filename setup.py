#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Olena K",
    author_email='olena.gull@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="To test cookiecutter",
    entry_points={
        'console_scripts': [
            'my_cookiecutter=my_cookiecutter.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='my_cookiecutter',
    name='my_cookiecutter',
    packages=find_packages(include=['my_cookiecutter', 'my_cookiecutter.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/olenagull/my_cookiecutter',
    version='0.1.0',
    zip_safe=False,
)
