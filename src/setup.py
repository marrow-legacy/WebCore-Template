#!/usr/bin/env python
# encoding: utf-8

import sys, os

try:
    from distribute_setup import use_setuptools
    use_setuptools()

except ImportError:
    pass

from setuptools import setup, find_packages


if sys.version_info <= (2, 5):
    raise SystemExit("Python 2.5 or later is required.")


setup(
        name = "Project",
        version = "0.1",
        description = "",
        author = "Your Name Here",
        author_email = "you@example.com",
        url = "http://example.com/",
        
        install_requires = ['WebCore < 2.0'],
        packages = find_packages(),
        
        zip_safe = False,
        include_package_data = True,
        package_data = {
                '': ['README.textile', 'LICENSE'],
                'project': ['templates/*']
            },
        
        paster_plugins = ['PasteScript', 'WebCore'],
    )
