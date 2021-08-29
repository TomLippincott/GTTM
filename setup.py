#!/usr/bin/env python

from distutils.core import setup

setup(name="GTTM",
      version="0.0.1",
      description="Geospatial Temporal Topic Models",
      long_description="",
      author="Tom Lippincott",
      author_email="tom@cs.jhu.edu",
      maintainer="Tom Lippincott",
      maintainer_email="tom@cs.jhu.edu",
      packages=["GTTM"],
      install_requires=["torch", "numpy", "sklearn", "pandas", "matplotlib", "bokeh"],
     )
