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


from object import object

class NativeMainLoop(object):
    """
    Object representing D-Bus main loop integration done in native code.
    Cannot be instantiated directly.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


