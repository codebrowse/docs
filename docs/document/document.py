"""Base class for a document object

Examples
--------

### Ex 1. Constructing a document
    >>> document = Document(name='document', filename=__file__)
    >>> document.filename in (
    ...  'docs/document/document.py',
    ...  'docs/document/document.pyc'
    ...  )
    True

"""
import ast
import codecs
import os

__author__ = ['Michael Van Veen (michael@mvanveen.net)']


class Document(object):
  """Base class for a document object"""

  #TODO: property for python path
  _doc_type = 'doc'
  def __init__(self, name=None, filename=None, source=None,
              _type=None, doc_type=None, *args, **kw):
    super(Document, self).__init__()
    self._filename = self._get_filename(filename, name)
    self._name = self._get_name(filename, name)
    self._type = _type

    self._source = self._get_source(source)


  def _get_filename(self, filename, name):
    """Private method called by constructor to setup filename"""
    if filename:
      return str(filename)


    elif name:
      return os.path.abspath(
        os.path.join(os.getcwd(), '.'.join((name,'py')))
      )


  def _get_name(self, filename, name):
    """Private method called by constructor to setup name"""
    if name:
      #TODO: custom exception
      return name

    elif filename:
      file_tuple = os.path.splitext(os.path.split(filename)[-1])
      #TODO: handle conversion from python path str to filestr
      return file_tuple[0]


  def _get_source(self, source):
    """Private method called by constructor to setup name"""
    if source:
      return source

    elif self._filename is not None:
      with self.open('r') as file_obj:
        return file_obj.read()


  @property
  def filename(self):
    """Represents the filename for a document"""
    # TODO: make sure it's not a python path
    if self._filename:
      return os.path.relpath(self._filename)
    else:
      return None


  @property
  def name(self):
    """Represents an identifier for a document"""
    return self._name


  @property
  def source(self):
    """Represents the source code for a document"""
    return self._source


  def parse(self):
    """Returns parsed AST for a document
    """
    return ast.parse(self._source)


  @property
  def parsed(self):
    """Returns the parsed AST for a document (as a property)."""
    return self.parse()


  @property
  def source(self):
    """Returns source code for a document
    """
    return self._source


  def open(self, *args, **kw):
    """Returns a file object of the file name."""

    #TODO: make exception
    assert self.filename
    self._file_obj = open(self.filename, *args, **kw)

    return self._file_obj


  def __repr__(self, *args, **kw):
    doc_type = 'doc'
    if self._type:
      doc_type = self._doc_type

    return '<[%s] %s>' % (doc_type, self._name)


  def __str__(self, *args, **kw):
    return self.source
