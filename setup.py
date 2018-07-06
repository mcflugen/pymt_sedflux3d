#! /usr/bin/env python
import os, sys

from setuptools import setup, find_packages

# from Cython.Build import cythonize
from distutils.extension import Extension
import numpy as np
import versioneer

from model_metadata.utils import get_cmdclass, get_entry_points


include_dirs = [
    np.get_include(),
    os.path.join(sys.prefix, "include"),
]


libraries = [
        "bmi_sedflux3d",
]


library_dirs = [
]


define_macros = [
]

undef_macros = [
]


extra_compile_args = [
]


ext_modules = [
    Extension(
        "sedflux3d._sedflux3d",
        ["sedflux3d/_sedflux3d.pyx"],
        language="c",
        include_dirs=include_dirs,
        libraries=libraries,
        library_dirs=library_dirs,
        define_macros=define_macros,
        undef_macros=undef_macros,
        extra_compile_args=extra_compile_args,
    )
]


packages = find_packages(include=["sedflux3d"])
pymt_components = [
    (
        "Sedflux3d=sedflux3d:Sedflux3d",
        "meta",
    )
]

setup(
    name="sedflux3d",
    author="Eric Hutton",
    description="Python interface to sedflux3d",
    version=versioneer.get_version(),
    setup_requires=["cython"],
    ext_modules=ext_modules,
    packages=packages,
    cmdclass=get_cmdclass(pymt_components, cmdclass=versioneer.get_cmdclass()),
    entry_points=get_entry_points(pymt_components),
)
