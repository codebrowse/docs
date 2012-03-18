"""Visitor mix-in for classes"""

import ast

from docs.visitors.query import QueryConstructor

class ClassVisitor(object):
  # TODO: make the fact that we need self._ast_obj and self.parsed
  # explicit.

  @property
  def classes(self):
    from docs.classes import Class

    functions = QueryConstructor(ast.ClassDef)
    functions.visit(self.parsed)

    return [Class(x) for x in
      sorted(
        functions.results,
        key=lambda x: x.lineno
    )]
