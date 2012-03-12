import unittest

from docs.imports import Import
from docs.module import Module

class TestImport(unittest.TestCase):
  def test_construct_mod(self):
    mod = Module(filename=__file__)
    #assert mod.imports


  def test_from_import_a(self):
    mod = Module(filename='test/imports/from_import_a.py')
    _import = mod.imports[0]

    #print _import.module
    assert _import._import == __import__('docs')
    print _import.name
    assert False
    assert _import.name
