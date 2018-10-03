#! /usr/bin/env python

from .bmi import Sedflux3D


__all__ = ["Sedflux3D"]

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
