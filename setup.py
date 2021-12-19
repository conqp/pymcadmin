#! /usr/bin/env python
"""Installation script."""

from setuptools import setup

setup(
    name='pymcadmin',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    author='Richard Neumann',
    author_email='mail@richard-neumann.de',
    python_requires='>=3.9',
    packages=['pymcadmin'],
    install_requires=[],
    entry_points={
        'console_scripts': [],
    },
    url='https://github.com/conqp/pymcadmin',
    license='GPLv3',
    description='A web-based Minecraft server manager.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    keywords='minecraft python server manager'
)
