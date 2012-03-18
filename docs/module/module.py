"""Wrapper object for Python modules"""

import ast
import inspect

from docs.imports import Import
from docs.visitors.base import VisitorBase
from docs.visitors.query import QueryConstructor

__author__ = ['Michael Van Veen (michael@mvanveen.net)']
METADATA = [
  'copyright', 'credits', 'license', 'version', 'maintainer',
  'email',  'status'
]

class Module(VisitorBase):
  """Represents the data model for a Python module"""

  def __init__(self, ast_node=None, source=None, path=None, filename=None):
    if filename:
      with open(filename, 'r') as file_obj:
        source = file_obj.read()
      ast_node = ast.parse(source)
      self._filename = filename
      self._path = path

    elif path:
      source = inspect.getmodule()
      ast_node = ast.parse(self._source)
      self._filename = inspect.getsourcefile(Import(path=path)._import)
      self._path = path

    else:
      self._path = None
      self._filename = None

    if ast_node and not isinstance(ast_node, ast.Module):
      raise TypeError('Expected an ast.Module object')

    super(Module, self).__init__(ast_node=ast_node, source=source)

    map( # set metadata properties on the object
      lambda x: setattr(self, x, self.get_var('__' + x + '__')),
      METADATA
    )
    self._type = 'Module'


  def __repr__(self, *args, **kw):
    return '<[Module] %s>' % (self.name, )


  def __str__(self, *args, **kw):
    return self.source


  @property
  def path(self):
    return self._path


  @property
  def filename(self):
    return self._filename


  @property
  def name(self):
    return self._path or self._filename or ''


  def get_var(self, var):
    """Helper for getting module metadata like __author__"""

    variables = QueryConstructor(ast.Name, id=var)
    variables.visit(self.parsed)

    if variables.results:
      result = variables.results[0].parent.value

    else:
      return []

    if isinstance(result, ast.Str):
      return [result.s]

    elif isinstance(result, ast.List):
      return [x.s for x in result.elts]

    return []


  @property
  def authors(self):
    """Returns a list of authors of a module"""
    author = self.get_var('__author__')
    authors = self.get_var('__authors__')
    return author + authors


  @property
  def assignments(self):
    """Lists the assignments declared in the module.

    Always returns a list.
    """
    return QueryConstructor(ast.Assign)
