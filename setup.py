from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

setup(name='basecalc',
    version=version,
    description="Convert numbers between various bases",
    long_description="""\
This module facilitates the conversion of numbers between various number bases. You may define your own digit sets, or use any of several predefined digit sets.
""",
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='base convert number',
    author='Craftworks',
    author_email='craftworks.jp+pypi@gmail.com',
    url='https://github.com/Craftworks/python-basecalc',
    license='GPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
    # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)
