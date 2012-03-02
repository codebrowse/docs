"""Base class for a document object

All Documents have the following attributes:

- `name`: Represents an identifier for the object.
- `filename`: File path

    >>> document = Document('file', 'file.py', 42)
    >>> document.filename
    'file.py'
    >>>
"""

__author__ = ['Michael Van Veen (michael@mvanveen.net)']

class Document(object):
  """Base class for a document object"""

  filename = str()
  name = str()

  def __init__(self, name=None, filename=None, line_no=None, source=None):
    self.name = name and unicode(name) or None
    self.source = name and unicode(name) or None

    self.filename = filename and str(filename) or None
    self.line_no = line_no and unicode(line_no) or None


  def open(self, *args, **kw):
    """Returns a file object of the file name.

    >>> document = Document('file', 'file.py')
    >>> with document.open('r') as file_obj:
    >>>   print file_obj.read()
    >>>
    """
    return open(self.filename, *args, **kw)

