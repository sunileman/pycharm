# encoding: utf-8
# module lxml.etree
# from /usr/lib64/python2.7/site-packages/lxml/etree.so
# by generator 1.136
"""
The ``lxml.etree`` module implements the extended ElementTree API
for XML.
"""

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>

from SchematronError import SchematronError

class SchematronValidateError(SchematronError):
    """ Error while validating an XML document with a Schematron schema. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __qualname__ = 'SchematronValidateError'


