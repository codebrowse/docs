"""Wrapper object for Python modules"""

import ast

from docs.document import Document
from docs.imports import Import
from docs.visitors.query import QueryConstructor

__author__ = ['Michael Van Veen (michael@mvanveen.net)']
METADATA = [
  'copyright', 'credits', 'license', 'version', 'maintainer',
  'email',  'status'
]

class Module(Document):
  """Represents the data model for a Python module"""

  def __init__(self, *args, **kw):
    super(Module, self).__init__(*args, **kw)

    map( # set metadata properties on the object
      lambda x: setattr(self, x, self.get_var('__' + x + '__')),
      METADATA
    )
    self._type = 'Module'


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
  def docstring(self):
    """Returns the module-level docstring."""
    return ast.get_docstring(self.parsed)


  @property
  def functions(self):
    """Lists the functions defined in the module

    Always returns a list.
    """
    functions = QueryConstructor(ast.FunctionDef)
    functions.visit(self.parsed)

    return functions.results


  @property
  def imports(self):
    """Lists the imports declared in the module

    Always returns a list.
    """
    imports = QueryConstructor(ast.Import)
    import_froms = QueryConstructor(ast.ImportFrom)

    imports.visit(self.parsed)
    import_froms.visit(self.parsed)

    return [Import(x) for x in
      sorted(
        imports.results + import_froms.results,
        key=lambda x: x.lineno
    )]


  @property
  def assignments(self):
    """Lists the assignments declared in the module.

    Always returns a list.
    """
    return QueryConstructor(ast.Assign)
