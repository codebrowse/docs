"""Unit tests for Document objects.  No pun inteded in filename."""

import os

from docs.document import Document

__author__ = 'Michael Van Veen (michael@mvanveen.net)'

file_path = os.path.relpath(
  os.path.join(os.path.abspath(__file__), '../', 'file.py')
)


def test_document_filename():
  doc = Document(filename=file_path)
  print doc.filename
  assert doc.filename == file_path, 'Did not receive expected path'


def test_document_name_construct_filename():
  doc = Document(filename=file_path)

  assert doc.name == 'file', 'Expected document name to be set correctly'


def test_document_lineno_none():
  doc = Document(filename=file_path)

  assert not doc.line_no, 'the line number should not be set'


def test_document_source_construct_filename():
  doc = Document(filename=file_path)

  with open(file_path, 'r') as file_obj:
    file_str = file_obj.read()

  assert file_str == doc.source, 'did not get expected source code result'


def test_open_document():
  doc = Document('file', file_path)

  with doc.open('r') as file_obj:
    file_str = file_obj.read()

  assert file_obj, 'Expected string!'


def test_repr():
  doc = Document('file')

  assert str(doc) == '<[doc] file>', 'did not get expected repr result'

