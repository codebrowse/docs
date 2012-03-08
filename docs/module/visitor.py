"""ASTVisitor for a Python Module"""

import ast

__author__ = ['Michael Van Veen (michael@mvanveen.net)']

class ModuleVisitor(ast.NodeVisitor):
  """Module-level AST visitor

  Visits Python modules and backs out documentation annotaitons.
  """
  def __init__(self, *args, **kw):
    super(ModuleVisitor, self).__init__(*args, **kw)
    self._functions = []
    self._classes   = []
    self._doc = ''

  def get_doc(self):
    """Gets the module-level docstring."""
    pass


  def visit_FunctionDef(self, node):
    self._functions.append(node)


  def visit_ClassDef(self, node):
    self._classes.append(node)


