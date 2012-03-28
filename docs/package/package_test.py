import unittest

import docs
from docs.package import Package

def test_cosntruct_package():
  assert Package(filename='docs/'), 'Could not successfully construct package'


class PackageTest(unittest.TestCase):
  def setUp(self, *args, **kw):
    self._pak = Package(filename='docs/')


  def test_get_packages(self):
    assert Package('docs/classes') in self._pak.packages, \
      "Expected docs/classes to be in packages attribute"


  def test_get_modules(self):
    assert docs.get(path='docs') in self._pak.modules, \
      "Expected docs __init__.py file to be in modules attribute"


  def test_get_packages(self):
    import os
    assert os in [x._import for x in self._pak.imports]
