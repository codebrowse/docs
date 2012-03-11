"""Unit tests for Document objects.  No pun inteded in filename."""
import inspect
import os

from docs.document import Document

__author__ = 'Michael Van Veen (michael@mvanveen.net)'

file_path = __file__

def test_document_filename():
  doc = Document(filename=file_path)
  assert doc.filename == os.path.relpath(file_path), 'Did not receive expected path'


def test_document_name_construct_filename():
  doc = Document(filename=file_path)

  assert doc.name == 'document_test', 'Expected document name to be set correctly'


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


def test_str():
  doc = Document('file', filename=file_path)
  with open(__file__, 'r') as file_obj:
    assert str(doc) == file_obj.read()
