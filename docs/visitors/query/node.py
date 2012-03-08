class Node(object):
  """AST Node wrapper object

  ** Wrap the module object for an AST **

      >>> import ast
      >>> import inspect
      >>> a = ast.parse(inspect.getsource(ast))
      >>> assert isinstance(a, ast.Module)
      >>> a = Node(a)
      >>> assert a.body
  """

  def __init__(self, ast_obj, *args, **kw):
    super(Node, self).__init__(*args, **kw)

    if hasattr(ast_obj, '_fields'):
      self._fields = ast_obj._fields

    if hasattr(ast_obj, '_attributes'):
      self._attributes = ast_obj._attributes

    for item in (self._fields, self._attributes):
      map(lambda x: setattr(self, '_' + x, getattr(ast_obj, x)), item)


  def __getattribute__(self, x):
    if hasattr(self, '_' + x):
      return super(Node, self).__getattribute__('_' + x)
    return super(Node, self).__getattribute__(x)

