import ast

from docs.util import indentation
from docs.visitors._class import ClassVisitor
from docs.visitors.function import FunctionVisitor
from docs.visitors._import import ImportVisitor
from docs.visitors.node import Node
from docs.visitors.query import QueryConstructor


class NoSourceCodeError(Exception):
  def __init__(self, *args, **kw):
    super(NoSourceCodeError, self).__init__(*args, **kw)

  def __str__(self, *args, **kw):
    return 'Source code is not defined, as we have only received an AST object!'


class VisitorBase(ClassVisitor, FunctionVisitor, ImportVisitor):
  """Base class for Module, Function, and Class types

  Provides properties for:

    - AST object
    - docstring
    - imports
    - functions
    - source code
  """

  def __init__(self, ast_node=None, source=None, *args, **kw):
    self._source = source
    self._parsed = None

    if self._source:
      self._indent_length = indentation.indent_length(self._source)
    else:
      self._indent_length = None

    if not ast_node and self._source:
      ast_node = ast.parse(self.source)

    elif ast_node:
      if isinstance(ast_node, Node):
        self._parsed = ast_node._ast_obj
      elif isinstance(ast_node, ast.AST):
        self._parsed = ast_node

      else:
        raise TypeError('ast_node must be an ast.AST or Node type!')

    else:
      raise TypeError('Need either source code or an ast object')

    if not isinstance(ast_node, Node):
        ast_node = Node(ast_node)

    super(VisitorBase, self).__init__()


  def __str__(self, *args, **kw):
    if not self._source:
      raise NoSourceCodeError

    return self._source


  def parse(self):
    """Returns parsed AST for a document
    """
    if not self._parsed:
      assert self._source
      self._parsed = ast.parse(self._source)

    return self._parsed


  @property
  def parsed(self):
    """Returns the parsed AST for a document (as a property)."""
    return self.parse()


  @property
  def source(self):
    """Source code of tree from the root node"""
    if not self._source:
      raise NoSourceCodeError

    return '\n'.join([
      x[self._indent_length:] for x in self._source.split('\n')
    ])


  @property
  def docstring(self):
    """Returns the module-level docstring."""
    return ast.get_docstring(self.parsed)

  def __eq__(self, other):
    return self.source == other.source
