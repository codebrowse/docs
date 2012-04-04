"""Encapsulates a Python package"""

import ast
import glob
import os

import docs
from docs.modules import Module


class Package(object):
  """Represents the data module for a Python package.

  - modules (modules in the package)
  - subpackages

  - imports   (from __init__.py)
  - functions (from __init__.py)
  - classes   (from __init__.py)
  """

  def __init__(self, filename=None):
    if not filename:
      raise ValueError

    assert os.path.isdir(filename)

    self._dir = filename

    filenames = glob.glob(os.path.join(self._dir, '__init__.py'))

    assert len(filenames) == 1, \
      'There should be one and only one __init__.py file in this directory.'

    self._init_file = Module(filename=os.path.abspath(filenames[0]))
    self._modules = None
    self._packages = None


  def __repr__(self, *args, **kw):
    return '<[Package] %s>'% (self._dir, )


  def __eq__(self, other):
    if not isinstance(other, Package):
      raise TypeError('Expected a Package object.')

    return self._dir == other._dir


  def _get_packages(self):
    has_init_file = lambda x: os.path.exists(
      os.path.join(self._dir, x, '__init__.py')
    )

    return [
      Package(filename=os.path.join(self._dir, directory ))
        for directory in os.listdir(self._dir) if os.path.isdir(
          os.path.join(self._dir, directory)
        ) and has_init_file(directory)
    ]


  def _get_modules(self):
    return [
      Module(filename=x) for x in  glob.glob(os.path.join(self._dir, '*.py'))
    ]


  @property
  def init_file(self, *args, **kw):
    return self._init_file

  @property
  def authors(self, *args, **kw):
    return self._init_file.authors


  @property
  def copyright(self, *args, **kw):
    return self._init_file.copyright


  @property
  def license(self, *args, **kw):
    return self._init_file.license


  @property
  def version(self, *args, **kw):
    return self._init_file.version


  @property
  def email(self, *args, **kw):
    return self._init_file.email


  @property
  def status(self, *args, **kw):
    return self._init_file.status


  @property
  def packages(self, *args, **kw):
    if not self._packages:
      self._packages = self._get_packages()

    return self._packages


  @property
  def modules(self, *args, **kw):
    if not self._modules:
      self._modules = self._get_modules()
    return self._modules


  @property
  def docstring(self, *args, **kw):
    return self._init_file.docstring


  @property
  def source(self, *args, **kw):
    return self._init_file.source


  @property
  def functions(self, *args, **kw):
    return self._init_file.functions


  @property
  def imports(self, *args, **kw):
    return self._init_file.imports
