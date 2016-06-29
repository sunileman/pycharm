# encoding: utf-8
# module _dbus_bindings
# from /usr/lib64/python2.7/site-packages/_dbus_bindings.so
# by generator 1.136
"""
Low-level Python bindings for libdbus. Don't use this module directly -
the public API is provided by the `dbus`, `dbus.service`, `dbus.mainloop`
and `dbus.mainloop.glib` modules, with a lower-level API provided by the
`dbus.lowlevel` module.
"""

# imports
import dbus.lowlevel as __dbus_lowlevel


from _IntBase import _IntBase

class Int32(_IntBase):
    """
    A signed 32-bit integer between -0x8000 0000 and +0x7FFF FFFF, represented as
    a subtype of `int`.
    
    Constructor::
    
        dbus.Int32(value: int[, variant_level: int]) -> Int32
    
    ``value`` must be within the allowed range, or `OverflowError` will be
    raised.
    
    ``variant_level`` must be non-negative; the default is 0.
    
    :IVariables:
      `variant_level` : int
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing an int32, this is represented in Python by an
        Int32 with variant_level==2.
    """
    def __init__(self, value, variant_level=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


