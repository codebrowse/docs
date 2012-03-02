'''Unit tests for Document objects.  No pun inteded in filename.
'''
import os

from docs.document import Document

__author__ = 'Michael Van Veen (michael@mvanveen.net)'

file_path = os.path.abspath(
  os.path.join(os.path.abspath(__file__), '../', 'file.py')
)

def test_open_document():
  doc = Document('file', file_path)
  with doc.open('r') as file_obj:
    file_str = file_obj.read()
  assert file_obj, 'Expected string!'


