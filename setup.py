from setuptools import setup, find_packages


requires = [
    "pyramid>=1.6dev",
    "zope.interface",
]

setup(
    name="rebecca.annotationmapper",
    namespace_packages=["rebecca"],
    install_requires=requires,
    packages=find_packages(),
    test_suite="rebecca.annotationmapper",
)