"""Nodes are a DAO (data access object) representation of ast.AST instances

DAO's are ast.AST instances which wrap existing AST instances in order to provide
some helpful accessors.

**Wrap the module object for an AST**

    >>> import ast
    >>> import inspect
    >>> a = ast.parse(inspect.getsource(ast))
    >>> assert isinstance(a, ast.Module)
    >>> a = Node(a)
    >>> assert a.body
"""
import ast

class Node(object):
  """AST Node wrapper object"""

  def __init__(self, ast_obj, parent=None, *args, **kw):
    super(Node, self).__init__(*args, **kw)

    if hasattr(ast_obj, '_fields'):
      self._fields = ast_obj._fields

    if hasattr(ast_obj, '_attributes'):
      self._attributes = ast_obj._attributes

    self._ast_obj = ast_obj
    self._parent = parent


  def __getattribute__(self, x):
    if hasattr(super(Node, self).__getattribute__('_ast_obj'), '_' + x):
      return super(Node, self).__getattribute__(
        '_ast_obj').__getattribute__('_' + x)

    elif hasattr(super(Node, self).__getattribute__('_ast_obj'), x):
      item = super(Node, self).__getattribute__('_ast_obj').__getattribute__(x)
      if isinstance(item, Node):
        return Node(item, parent=super(Node, self).__getattribute__('_ast_obj'))
      return item

    return super(Node, self).__getattribute__(x)


  def __repr__(self, *args, **kw):
    return '<[%s]>' % (self._ast_obj.__class__.__name__, )


  @property
  def parent(self):
    return self._parent
