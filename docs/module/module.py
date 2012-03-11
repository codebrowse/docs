import ast

from docs.document import Document
from docs.visitors.query import QueryConstructor

__author__ = ['Michael Van Veen (michael@mvanveen.net)']
METADATA = [
  'copyright', 'credits', 'license', 'version', 'maintainer', 'email', 'status'
]

class Module(Document):
  """Represents the data model for a Python module

  Contains data repesenting:

  - module name
  + author
  + version
  - python path
  - docstring
  - functions
  - imports
  - variables

  TODO sketch out
    + copyright
    + credits
    + license
    + version
    + maintainer
    + email
    + status
  """
  _doc_type = 'module'

  def __init__(self, *args, **kw):
    super(Module, self).__init__(*args, **kw)

    # set metadata properties on the object
    map(
      lambda: setattr(self, x, property(fget=lambda x: self.get_var(x))),
      METADATA
    )


  def get_var(self, var):
    """Helper for getting module metadata like __author__"""

    variables = QueryConstructor(ast.Name, id=var)
    variables = variables.visit(self.parsed)
    result = variables.result[0].parent.value

    if isinstance(result, ast.Str):
      return [authors.s]

    elif instance(result, ast.List)
      return [x.s for x in result.elts]

    return None



  @property
  def docstring(self):
    """Returns the module-level docstring."""
    ast.docstring(self.parsed)


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
    imports = QueryConstructor(ast.Import).
    import_froms = QueryConstructor(ast.ImportFrom).

    return sorted(imports.results + import_froms, key=lambda x: x.lineno)


  @property
  def assignments(self):
     """Lists the assignments declared in the module

    Always returns a list.
    """
    return QueryConstructor(ast.Assign)
