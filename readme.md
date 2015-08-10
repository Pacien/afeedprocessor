A feed processor
================

`A feed processor` is a simple Python framework for RSS feeds processing, providing classes with overridable methods 
for easy alteration.

It includes `a feed parser`, which parses RSS[0.90:2.0], Atom[0.3:1.0] and CDF feeds into Python objects.


Purposes
--------

`A feed processor` can be used to programmatically remove advertisements from RSS feeds for instance.

Since it is written in Python, this framework can be embedded in a scriptable RSS reader or used to make short CGI 
proxy scripts.


Usage
-----

The file `example.py` contains an example of a custom feed processor which performs light modifications on a public RSS 
feed.


Dependencies
------------

`A feed processor` is written in Python 3 and depends on `PyRSS2Gen` and `feedparser`, which are both available as 
pip and distros packages.


License
-------

`A feed processor` is a free software distributed under the terms of the provided GNU Affero General Public License.


TODO list
---------

- [x] add an example
- [ ] add some documentation
- [ ] make a pip package
- [ ] make distros packages?
