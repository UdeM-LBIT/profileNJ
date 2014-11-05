#!/usr/bin/env python
#
# setup for profileNJ library packages
#
# use the following to install:
#   python setup.py build
#   python setup.py install
#

import setuptools
import os, sys

if os.path.exists('README'):
	README = open('README').read()
else:
	README = ""  # a placeholder, readme is generated on release

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), "python")))
from PolytomySolver import __project__, __version__

setuptools.setup(
	name=__project__,
	version=__version__,

	description="profileNJ correct polytomies in tree, using minimum reconciliation (with specietree) cost, and Neighbor-Joining algorithm for clustering",
	url='https://github.com/UdeM-LBIT/python-tree-processing',
	author='Emmanuel Noutahi',
	author_email='emmanuel.noutahi@hotmail.ca',
	scripts = ['bin/profileNJ'],

	packages=setuptools.find_packages(),

	entry_points={'console_scripts': []},

	long_description=(README + '\n'),
	license='WTFPL',
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Environment :: Console',
		'Natural Language :: English',
		'Intended Audience :: Developers',
		'Intended Audience :: Education',
		'Intended Audience :: Science/Research',
		'License :: OSI Approved :: GNU General Public License (GPL)',
		'Operating System :: POSIX',
		'Programming Language :: Python',
	],

	install_requires=[
		'ete2',
		'numpy',
		'lxml'
	]
)