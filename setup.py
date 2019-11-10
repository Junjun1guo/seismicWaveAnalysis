from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name = 'waveAnalysis',
    version = '0.0.3',
    keywords = ('simple', 'test'),
    description = 'seismic wave analysis',
    license = 'MIT License',

    author = 'Junjun Guo',
    author_email = 'guojj_ce@163.com',

    packages = find_packages(),
    platforms = 'any',
)