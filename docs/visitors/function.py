"""Visitor mix-in for functions
"""
import ast

from docs.visitors.query import QueryConstructor

class FunctionVisitor(object):
  # TODO: make the fact that we need self._ast_obj and self.parsed
  # explicit.

  @property
  def functions(self, **kw):
    from docs.function.function import Function

    functions = QueryConstructor(ast.FunctionDef, **kw)
    functions.visit(self.parsed)

    return [Function(x) for x in
      sorted(
        functions.results,
        key=lambda x: x.lineno
    )]
