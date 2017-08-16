from setuptools import setup

setup(
    name='raktar',
    version='0.1',
    description='Electronic Parts Database Utilities',
    url='http://github.com/mokerek/raktar/utilities',
    author='Mokerek',
    author_email='N/A',
    packages=['raktar'],
    install_requires=['pyyaml'],
    entry_points={
        'console_scripts': [
            'raktar-check=raktar.check:main'
        ]
    },
    zip_safe=False
)
