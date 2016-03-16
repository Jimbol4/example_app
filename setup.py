
from setuptools import setup, find_packages
import sys, os

setup(name='example_app',
    version='1.0',
    description="Example app",
    long_description="Example app",
    classifiers=[],
    keywords='',
    author='James Thompson',
    author_email='james.thompson@jellyfish.co.uk',
    url='http://example.com',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    install_requires=[
        ### Required to build documentation
        # "Sphinx >= 1.0",
        ### Required for testing
        # "nose",
        # "coverage",
        ### Required to function
        'cement',
        ],
    setup_requires=[],
    entry_points="""
        [console_scripts]
        example_app = example_app.cli.main:main
    """,
    namespace_packages=[],
    )
