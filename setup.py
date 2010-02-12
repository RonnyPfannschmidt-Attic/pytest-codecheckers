from setuptools import setup

setup(
    name='pytest-codecheckers',
    description='pytest addon to add code-checking as source for testcases',
    version='0.0',
    author='Ronny Pfannschmidt',
    author_email='Ronny.Pfannschmidt@gmx.de',
    packages=[
        'codecheckers',
        ],
    entry_points = {
        'pytest11': [
            'codechecker = codecheckers.plugin',
            ],
        'codechecker': [
            'pep8 = codecheckers.pep',
            'pyflakes = codecheckers.flakes',
            ],
        },
    install_requires=[
        'pyflakes>=0.4',
        'pep8',
        ],
    )
