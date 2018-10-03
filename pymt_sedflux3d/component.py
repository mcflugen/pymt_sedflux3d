from __future__ import absolute_import

from pymt.framework.bmi_bridge import bmi_factory

from .bmi import Sedflux3D

Sedflux3D = bmi_factory(Sedflux3D)

del bmi_factory
