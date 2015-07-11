from setuptools import setup, find_packages
import os

__author__ = 'Atsushi Odagiri'
__author_email__ = 'aodagx@gmail.com'
__version__ = '0.0'


here = os.path.dirname(__file__)

requires = [
    "pyramid>=1.6dev",
    "zope.interface",
]


def read(name):
    try:
        with open(os.path.join(here, name)) as f:
            return f.read()
    except:
        return ""


setup(
    name="rebecca.annotationmapper",
    author=__author__,
    author_email=__author_email__,
    version=__version__,
    license='MIT',
    url='https://github.com/rebeccaframework/rebecca.annotationmapper',
    namespace_packages=["rebecca"],
    description='annotation view mapper for pyramid',
    long_description=read("README.rst"),
    install_requires=requires,
    packages=find_packages(),
    test_suite="rebecca.annotationmapper",
)