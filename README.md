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

### Modules

    >>> from docs.modules import Module
    >>> m = Module(filename='docs/modules/module.py')
    >>> m
    <[Module] docs/modules/module.py>

**Authors**
    >>> import docs
    >>> d = docs.get(docs)
    >>> d.authors
    ['Michael Van Veen (michael@mvanveen.net)']

**Docstrings**
    
    >>> m.docstring
    'Wrapper object for Python modules'

**Version**

     >>> d = docs.get(docs)
     >>> d.version
     ['0.1']

**Copyright**

     >>> d = docs.get(docs)
     >>> d.copyright
     ['Copyright 2012, Michael Van Veen']
    
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
    'docs/__init__.py'

### Functions

**Top-level accessor**

    >>> import docs
    >>> len(docs.get_functions(docs))
    4

**Object Attributes**

The `functions` attribute is defined for `Function`, `Module`, and `Class`.

    >>> d = docs.get(docs)
    >>> d.functions
    [<[Function] get>, <[Function] get_imports>, <[Function] get_functions>, <[Function] get_classes>]
    

### Imports

**Top-level accessor**

    >>> import docs
    >>> docs.get_imports(docs)
    [<[Import] ast>, <[Import] inspect>, <[Import] os>, <[Import] sys>, <[ImportFrom] docs.classes.Class>, <[ImportFrom] docs.function.Function>, <[ImportFrom] docs.imports.Import>, <[ImportFrom] docs.visitors.Node>, <[ImportFrom] docs.modules.Module>, <[ImportFrom] docs.package.Package>]
    
**Object Attributes**

    >>> d = docs.get(docs)
    >>> len(d.imports)
    10


### Classes

**Top-level accessor**

    >>> import docs
    >>> docs.get_classes('ast')
    [<[Class] NodeVisitor>, <[Class] NodeTransformer>]

**Object Attributes**

    >>> d = docs.get('ast')
    >>> d.classes
    [<[Class] NodeVisitor>, <[Class] NodeTransformer>]



*Coming soon:*

- Variables
- python paths and filenames across all 

*Nice to haves:*

- Support for Statement and Expression
- Dynamic import hooks
- comments
- TODOS
- JSON API?
- ???
- Profit
      
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
