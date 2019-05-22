"""
``cello2`` is a module that reads a netlist in the Cello2 JSON format
into a Python class structure.
"""

import sys

__version__ = '0.0.1'

if not (sys.version_info.major == 3):
    raise ImportError("pycello2 requires Python 3")

del sys