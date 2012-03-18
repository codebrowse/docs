[![Build Status](https://secure.travis-ci.org/mvanveen/docs.png?branch=master)](http://travis-ci.org/mvanveen/docs)

Python Docs
===========

#### A Python Documentation API for Developers####

Michael Van Veen

![Machine Simple](https://github.com/mvanveen/docs/raw/master/press.jpg)

## Abstract

Python has wonderful, first-class support for documentation.  Unfortunately, 
this incredibly thoughtful feature of the language is hidden behind large, 
monolithic suites or outdated, unsupported pieces of spaghetti.  Up until now, 
we haven't had easy programatic access to our source code and documentation.  

No longer.  Docs is a Python Documentation API I for Developers.  Our language 
is dynamic.  It's time for our documentation to start acting like it.

### Warning

It is early days for this project.  There is still a *lot* of stuff 
to be done.  Among those are several security concerns.  Most importantly, 
*note that Python Docs will import the modules and objects you throw at it (and 
probably will for a long time), so please only use it with modules that you trust!*

## Examples


### Functions

**Top-level accessor**

    >>> import docs
    >>> len(docs.functions(docs))
    4

**Object Attributes**

The `functions` attribute is defined for `Function`, `Module`, and `Class`.

    >>> d = docs.get(docs)
    >>> d.functions()
    [<[Function] get>, <[Function] imports>, <[Function] functions>, <[Function] classes>]

### Imports

**Top-level accessor**

    >>> import docs
    >>> docs.imports(docs)

**Object Attributes**

    >>> d = docs.get(docs)
    >>> len(docs.imports(docs))
    9


### Classes

**Top-level accessor**

    >>> import docs
    >>> docs.classes('ast')
    [<[Class] NodeVisitor>, <[Class] NodeTransformer>]

**Object Attributes**

    >>> d = docs.get('ast')
    >>> d.classes
    [<[Class] NodeVisitor>, <[Class] NodeTransformer>]

### Parsing

**Access anything within `sys.path`**

    >>> import docs
    >>> docs.get('ast')
    < [Module] pydoc>

**Parse file objects**

    >>> docs.get(filename='file.py')
    < [Module] file.py>

**Parse live objects**

    >>> docs.get(docs)
    < [Module] docs/__init__.py>

## Features

Python Docs currently provides easy access to modules and imports.  Functions and 
classes are on the way, and support for statements and expressions is in the roadmap.

Stay tuned!


### Modules

    >>> from docs.module import Module
    >>> m = Module(filename='docs/module/module.py')
    >>> m
    <[Module] docs/module/module.py>

**Authors**
    
    >>> d = docs.get(docs)
    >>> d.authors
    >>> ['Michael Van Veen (michael@mvanveen.net)']

**Docstrings**
    
    >>> m.docstring
    'Wrapper object for Python modules 

**Version**

     >>> d = docs.get(docs)
     >>> d.version
     ['0.1']

**Copyright**

     >>> d = docs.get(docs)
     >>> d.copyright
     ['Copyright © 2012, Michael Van Veen']
    
**Maintainers**

    >>> d = docs.get(docs)
    >>> d.maintainers
    ['Michael Van Veen (michael@mvanveen.net)']

**Status**

    >>> d = docs.get(docs)
    >>> d.status
    ['Beta']
 
**Filename**

    >>> d = docs.get(docs)
    >>> d.filename
    docs/__init__.py



*Coming soon:*
- Variables
- Function Names
- python path


### Nice to haves:

- Support for Statement and Expression
- Dynamic import hooks
- comments
- TODOS
- JSON API?
- ???
- Profit

## FAQ

---

**Q:** What is your motivation behind Python Docs?

**A:** Python Docs is an attempt to create a great API to facilitate easy access to 
documentation and source primitives within Python.

My intent is to construct a solid base for the development of the 
documentation/refactoring libraries and tools I want to see for Python.

I hope that you find it useful for your own purposes!  Please feel free to contribute :-)

**Q:** Why not Sphinx?

**A:** **Disclaimer:** I have admittedly never really gotten that far into Sphinx. 
Please take the following with a grain of salt.

I think Python Docs & Sphinx have seperate, but mutually-beneficial goals.

Python Docs is a Documentation API.  Sphinx is a documention tool.  Documentation tools 
are just one possible use case for Python Docs.

**Q:** I don't get it.  Isn't having `__doc__ ` on objects enough?

**A:** Unfortunately, no!  `__doc__` is a great start, but it's simply not enough.  Just getting module-level docstrings, ends up being rather difficult, as modules don't have `__doc__` attributes.

In fact, `__doc__` attributes are only useful if you have a live object on your hands.  This is not always the case!  Python Docs attempts to support the various ways in which people attempt to parse documentation: as a live object, as an import available accessible from `sys.path`, or as a file object or string.

Furthermore, on its own, `__doc__` isn't entirely useful as a documentation API.  Python Docs attempts to give a more complete picture by providing other metadata like `__author__` and `__version__`, as well as other niceties like python paths, line numbers, file paths, attributes, and even the source!

**Q:** How are you able to support so many different types of parsing?

**A:** Python Docs uses an AST `NodeVisitor` class to directly parse the source code.  This handles most classes of source code parsing other than live objects.  The wonderful `inspect` module lets us get the source of live objects, so we've got our bases covered.

**Q:** Isn't importing arbitrary Python dangerous/against the principles of static analysis?

**A:** Yes, absolutely!  However, without it we lose a lot of flexibility.  Even `pydoc` ends up
importing at the end of the day.  Using `__import__` lends Python Docs a lot of power.  In 
general, static analysis in an environment as dynamic as Python is somewhat limiting, and Python 
Docs attempts to compromise by leveraging the import system infor what it's good for, namely 
resolving python paths to objects.
       
In the long term future of the project, I'd like to leverage static analysis as much as possible.
Python import hooks may provide a route to instrumenting source code execution in a way that lets
us keep our goal of staying pure.
      
-----

### Influences

- `Pydoc`, a somewhat hacky, ugly, yet incredibly wonderful Python documentation tool and `stdlib` module.
- [PEP 257][pep257], "Docstring Conventions"
- [PEP 345](http://www.python.org/dev/peps/pep-0345/), "Metadata for Python Software Packages 1.2"
- [http://mail.python.org/pipermail/python-dev/2001-March/013342.html](http://mail.python.org/pipermail/python-dev/2001-March/013342.html)
- [Docco](http://jashkenas.github.com/docco/), an excellent markdown-based literate programming tool, and [Tacco](https://github.com/mvanveen/Tacco), my unfinished sketch of a clone which uses docstrings.
- The wonderful `ast` and `inspect` modules.

### License

Source code is MIT licensed.  Documentation is creative commons <insert here>.

--mvv

[pep257]: http://www.python.org/dev/peps/pep-0257/
