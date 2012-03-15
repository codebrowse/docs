import ast

from docs.visitors.query import QueryConstructor


class ImportVisitor(object):

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

