"""Scanpy - Single-Cell Analysis in Python

See scanpy.api for the API.
"""

import sys
import warnings
from distutils.version import LooseVersion

# version generated by versioneer
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

if sys.version_info < (3, 0):
    warnings.warn('Scanpy only runs reliably with Python 3, preferrably >=3.5.')

import pandas as pd
if pd.__version__ < LooseVersion('0.21'):
    raise ImportError('Scanpy needs pandas version >=0.21, not {}.\n'
                      'Run `pip install pandas --upgrade`.'
                      .format(pd.__version__))

import anndata
# NOTE: pytest does not correctly retrieve anndata's version? why?
#       use the following hack...
if anndata.__version__ != '0+unknown':
    if anndata.__version__ < LooseVersion('0.5'):
        raise ImportError('Scanpy {} needs anndata version >=0.5, not {}.\n'
                          'Run `pip install anndata --upgrade`.'
                          .format(__version__, anndata.__version__))
