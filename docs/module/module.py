from docs.document import Document

__author__ = ['Michael Van Veen (michael@mvanveen.net)']

class Module(Document):
  """Represents the data model for a Python module

  Contains data repesenting:

  - function name
  - author
  - version
  - python path
  - docstring
  - functions
  - imports
  - variables

  TODO sketch out:
    - __copyright__
    - __credits__
    - __license__
    - __version__
    - __maintainer__
    - __email__
    - __status__
  """
  _doc_type = 'module'

  def __init__(self, *args, **kw):
    super(Module, self).__init__(*args, **kw)

  @propery
  def authors(self):
    """Returns the authors listed in the __authors__ global variable.

    Always returns a list.
    """
    pass


  @propery
  def version(self):
    """Returns the version number listed in the __version__ global variable."""
    pass


  @property
  def docstring(self):
    """Returns the module-level docstring."""
    pass


  @property
  def functions(self):
    """Lists the functions defined in the module

    Always returns a list.
    """
    pass


  @property
  def imports(self):
    """Lists the imports declared in the module

    Always returns a list.
    """
    pass


  @property
  def vars(self):
     """Lists the global variables declared in the module

    Always returns a list.
    """
    pass

