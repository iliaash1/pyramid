"""
The variables defined in compat are designed to provide
compatibility between Python 2 & 3. Each sub-module is specifically
designed not to make calls out to other portions of Pyramid and to
remove circular dependencies.
"""

from .python import *
from .numpy import *

__all__ = [s for s in dir() if not s.startswith('_')]
