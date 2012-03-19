"""Utilitles for Python indenation"""

from itertools import takewhile
import string


def indent_length(source):
  """Returns the amount of whitespace in a source variable

  >>> print indent_length('''
  ...   This is a test
  ...   Ah yeah
  ... ''')
  2
  """
  if not isinstance(source, basestring):
    raise TypeError

  source = source.split('\n')
  items = takewhile(
    lambda i: all([
      x[i] in string.whitespace for x in source if len(x) > i
    ]),
    range(len(source))
  )
  return len(list(items))
