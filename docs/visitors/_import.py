import ast

from docs.visitors.query import QueryConstructor


class ImportVisitor(object):

  @property
  def imports(self, **kw):
    """Lists the imports declared in the module

    Always returns a list.
    """
    from docs.imports import Import

    imports = QueryConstructor(ast.Import, **kw)
    import_froms = QueryConstructor(ast.ImportFrom, **kw)

    imports.visit(self.parsed)
    import_froms.visit(self.parsed)

    return [Import(x) for x in
      sorted(
        imports.results + import_froms.results,
        key=lambda x: x.lineno
    )]
