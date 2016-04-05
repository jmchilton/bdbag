#
# Copyright 2015 University of Southern California
# Distributed under the Apache License, Version 2.0. See LICENSE for more info.
#

""" Installation script for the BDBag utilities.
"""

from setuptools import setup, find_packages

setup(
    name="bdbag",
    description="Big Data Bag Utility",
    url='https://github.com/ini-bdds/bdbag/',
    maintainer='USC Information Sciences Institute ISR Division',
    maintainer_email='misd-support@isi.edu',
    version="0.1-prerelease",
    packages=find_packages(),
    package_data={'bdbag': ['profiles/*.*']},
    scripts=['bin/bdbag'],
    requires=[
        'cookielib',
        'csv',
        'datetime',
        'json',
        'optparse',
        'os',
        'os.path',
        'simplejson',
        'shutil',
        'sys',
        'zipfile',
        'tarfile',
        'tempfile',
        'urlparse',
        'xml'],
    install_requires=['ordereddict',
                      'requests',
                      'bagit==1.5.4.dev',
                      'bagit-profiles-validator==1.0.2'],
    dependency_links=[
         "http://github.com/ini-bdds/bagit-python/archive/master.zip#egg=bagit-1.5.4.dev",
         "http://github.com/ini-bdds/bagit-profiles-validator/archive/master.zip#egg=bagit-profiles-validator-1.0.2"
    ],
    license='Apache 2.0',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ])
