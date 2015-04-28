from setuptools import setup, find_packages
import os
import pylib

# http://bugs.python.org/issue8876#msg208792
del os.link

def prepend_find_packages(*roots):
    ''' Recursively traverse nested packages under the root directories
    '''
    packages = []
    
    for root in roots:
        packages += [root]
        packages += [root + '.' + s for s in find_packages(root)]
        
    return packages

setup(
    version = pylib.__version__,
    name = 'tfliss.github.io',
    author = 'Tim Fliss',
    author_email = 't.fliss@gmail.com',
    packages = prepend_find_packages('pylib'),
    package_data={'': ['*.md'] },
    description = 'Test github page',
    requires = [],
    tests_require=[],
    setup_requires=['setuptools', 'sphinx', 'numpydoc'],
    url='http://tfliss.github.io',
    scripts=[],
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7'
        ])
