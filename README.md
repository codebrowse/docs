Python Docs
===========

#### A Python Documentation API for Developers####

Michael Van Veen

![](https://github.com/mvanveen/docs/raw/master/press.jpg)


Python has wonderful, first-class support for documentation.  Unfortunately, this incredibly thoughtful feature of the language is hidden behind large, monolithic suites or outdated, unsupported pieces of spaghetti.

Up until now, we haven't had easy programatic access to our source code and documentation.  

No longer.  Docs is a Python Documentation API I for Developers.  Our language is dynamic.  It's time for our documentation to start acting like it.

## Features

Python Docs provides easy access to the following items:

### Modules
- author
- version
- python path
- file path
- docstring
- functions
- imports
- variables

### Functions

- function name
- definition location
- docstring

- globals
- locals

- imports

### Objects

- object name
- object type
- definition location
- docstring

- attributes
- items


### Nice to haves:

- comments
- TODOS
- JSON API?


## Examples

### Parsing

** Parse a live Python object **

    >>> import docs
    >>> docs.get(obj)
    < [object] obj>

** Access anything within sys.path **

    >>> import docs
    >>> docs.get(pydoc)
    < [module] pydoc>

** Parse file objects**

    >>> with open('file.py') as file_obj:
    >>>   docs.get(file_obj)
    < [module] file>

** …Or even strings! **

    >>> with open('file.py') as file_obj:
    >>>   docs.get(file_obj.read())
    < [module] str>


### Helpers

** Get summary line of docstring **

    >>> docstring.get(obj).docstring.summary
	'This is the summary line of this document's docstring'

** Get trimmed docstring (minus summary line) **

    >>> docstring.get(obj).docstring.trimmed
    """
    This is the remainder of this document's doctstring.  Lorem ipsum
    dolor etc. etc. etc.
    """

## FAQ

---

**Q:** What is your motivation behind Python Docs?

**A:**Python Docs is an attempt to create a great API to facilitate easy access to documentation and source primitives within Python.

My intent is to construct a solid base for the development of the documentation/refactoring libraries and tools I want to see for Python.

I hope that you find it useful for your own purposes!  Please feel free to contribute :-)

**Q:** Why not Sphinx?

**A:** **Disclaimer:** I have admittedly never really gotten that far into Sphinx.  Please take the following with a grain of salt.

I think Python Docs & Sphinx have seperate, but mutually-beneficial goals.

Python Docs is a Documentation API.  Sphinx is a documention tool.  Documentation tools are just one possible use case for Python Docs.

**Q:** I don't get it.  Isn't having `__doc__ ` on objects enough?

**A:** Unfortunately, no!  `__doc__` is a great start, but it's simply not enough.  Just getting module-level docstrings, ends up being rather difficult, as modules don't have `__doc__` attributes.

In fact, `__doc__` attributes are only useful if you have a live object on your hands.  This is not always the case!  Python Docs attempts to support the various ways in which people attempt to parse documentation: as a live object, as an import available accessible from `sys.path`, or as a file object or string.

Furthermore, on its own, `__doc__` isn't entirely useful as a documentation API.  Python Docs attempts to give a more complete picture by providing other metadata like `__author__` and `__version__`, as well as other niceties like python paths, line numbers, file paths, attributes, and even the source!

**Q:** How are you able to support so many different types of parsing?

**A:** Python Docs uses an AST `NodeVisitor` class to directly parse the source code.  This handles most classes of source code parsing other than live objects.  The wonderful `inspect` module lets us get the source of live objects, so we've got our bases covered.

-----

### Influences

- `Pydoc`, a somewhat hacky, ugly, yet incredibly wonderful Python documentation tool and `stdlib` module.
- [PEP 257][pep257], "Docstring Conventions"
- http://www.python.org/dev/peps/pep-0345/
- http://mail.python.org/pipermail/python-dev/2001-March/013342.html
- Docco, an excellent markdown-based literate programming tool, and Tacco, my unfinished sketch of a clone which uses docstrings.


### License

Source code is MIT licensed.  Documentation is creative commons <insert here>.