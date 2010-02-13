"""
py.test plugin for checking PEP8 source code compliance using pyflakes.

Usage
---------

after installation (e.g. via ``pip install pytest-codecheckers``) you can type::

    py.test [path/to/mypkg]

which will automatically perform source code sanity checks.  If you have
further questions please send them to the `pytest-dev`_ mailing list.

.. _`pytest-dev`: http://codespeak.net/mailman/listinfo/py-dev
"""
from setuptools import setup

setup(
    name='pytest-codecheckers',
    description='pytest plugin to add source code sanity checks (pep8 and friends)',
    long_description=__doc__,
    version='0.2',
    author='Ronny Pfannschmidt',
    author_email='Ronny.Pfannschmidt@gmx.de',
    url='http://bitbucket.org/RonnyPfannschmidt/pytest-codecheckers/',
    packages=[
        'codecheckers',
        ],
    entry_points={
        'pytest11': [
            'codechecker = codecheckers.plugin',
            ],
        'codechecker': [
            'pep8 = codecheckers.pep',
            'pyflakes = codecheckers.flakes',
            ],
        },
    install_requires=[
        'py>=1.2.0',
        'pyflakes>=0.4',
        'pep8',
        ],
    )
