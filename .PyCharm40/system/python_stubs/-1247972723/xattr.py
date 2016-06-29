# encoding: utf-8
# module xattr
# from /usr/lib64/python2.7/site-packages/xattr.so
# by generator 1.136
"""
This module gives access to the extended attributes present
in some operating systems/filesystems. You can list attributes,
get, set and remove them.

The module exposes two sets of functions:
  - the 'old' :func:`listxattr`, :func:`getxattr`, :func:`setxattr`,
    :func:`removexattr`
    functions which are deprecated since version 0.4
  - the new :func:`list`, :func:`get`, :func:`get_all`, :func:`set`,
    :func:`remove` functions
    which expose a namespace-aware API and simplify a bit the calling
    model by using keyword arguments

Example: 

  >>> import xattr
  >>> xattr.listxattr("file.txt")
  ['user.mime_type']
  >>> xattr.getxattr("file.txt", "user.mime_type")
  'text/plain'
  >>> xattr.setxattr("file.txt", "user.comment", "Simple text file")
  >>> xattr.listxattr("file.txt")
  ['user.mime_type', 'user.comment']
  >>> xattr.removexattr ("file.txt", "user.comment")

.. note:: Most or all errors reported by the system while using
   the ``xattr`` library will be reported by raising
   a :exc:`EnvironmentError`; under
   Linux, the following ``errno`` values are used:

   - ``ENOATTR`` and ``ENODATA`` mean that the attribute name is
     invalid
   - ``ENOTSUP`` and ``EOPNOTSUPP`` mean that the filesystem does not
     support extended attributes, or that the namespace is invalid
   - ``E2BIG`` mean that the attribute value is too big
   - ``ERANGE`` mean that the attribute name is too big (it might also
     mean an error in the xattr module itself)
   - ``ENOSPC`` and ``EDQUOT`` are documented as meaning out of disk
     space or out of disk space because of quota limits
.. note:: Under Python 3, the namespace argument is a byte string,
   not a unicode string.
"""
# no imports

# Variables with simple values

NS_SECURITY = 'security'
NS_SYSTEM = 'system'
NS_TRUSTED = 'trusted'
NS_USER = 'user'

XATTR_CREATE = 1
XATTR_REPLACE = 2

__author__ = 'Iustin Pop'

__contact__ = 'iusty@k1024.org'

__docformat__ = 'restructuredtext en'

__license__ = 'GNU Lesser General Public License (LGPL)'

__version__ = '0.5.1'

# functions

def get(item, name, nofollow=False, namespace=None): # real signature unknown; restored from __doc__
    """
    get(item, name[, nofollow=False, namespace=None])
    Get the value of a given extended attribute.
    
    Example:
        >>> xattr.get('/path/to/file', 'user.comment')
        'test'
        >>> xattr.get('/path/to/file', 'comment', namespace=xattr.NS_USER)
        'test'
    
    :param item: a string representing a file-name, or a file-like
        object, or a file descriptor; this represents the file on 
        which to act
    :param string name: the attribute whose value to retrieve;
        usually in the form of ``system.posix_acl`` or ``user.mime_type``
    :param nofollow: if true and if
        the file name given is a symbolic link, the
        function will operate on the symbolic link itself instead
        of its target; defaults to false
    :type nofollow: boolean, optional
    :param namespace: if given, the attribute must not contain the
        namespace, but instead it will be taken from this parameter
    :type namespace: bytes
    :return: the value of the extended attribute (can contain NULLs)
    :rtype: string
    :raises EnvironmentError: caused by any system errors
    
    .. versionadded:: 0.4
    .. versionchanged:: 0.5.1
       The namespace argument, if passed, cannot be None anymore; to
       explicitly specify an empty namespace, pass an empty
       string (byte string under Python 3).
    """
    pass

def getxattr(item, attribute, nofollow=False): # real signature unknown; restored from __doc__
    """
    getxattr(item, attribute[, nofollow=False])
    Get the value of a given extended attribute (deprecated).
    
    :param item: a string representing a file-name, or a file-like
        object, or a file descriptor; this represents the file on 
        which to act
    :param string name: the attribute whose value to retrieve;
        usually in the form of ``system.posix_acl`` or ``user.mime_type``
    :param nofollow: if true and if
        the file name given is a symbolic link, the
        function will operate on the symbolic link itself instead
        of its target; defaults to false
    :type nofollow: boolean, optional
    
    .. deprecated:: 0.4
       this function has been deprecated
       by the :func:`get` function.
    """
    pass

def get_all(item, nofollow=False, namespace=None): # real signature unknown; restored from __doc__
    """
    get_all(item[, nofollow=False, namespace=None])
    Get all the extended attributes of an item.
    
    This function performs a bulk-get of all extended attribute names
    and the corresponding value.
    Example:
    
        >>> xattr.get_all('/path/to/file')
        [('user.mime-type', 'plain/text'), ('user.comment', 'test'),
         ('system.posix_acl_access', '\x02\x00...')]
        >>> xattr.get_all('/path/to/file', namespace=xattr.NS_USER)
        [('mime-type', 'plain/text'), ('comment', 'test')]
    
    :param item: a string representing a file-name, or a file-like
        object, or a file descriptor; this represents the file on 
        which to act
    :keyword namespace: an optional namespace for filtering the
       attributes; for example, querying all user attributes can be
       accomplished by passing namespace=:const:`NS_USER`
    :type namespace: string
    :param nofollow: if true and if
        the file name given is a symbolic link, the
        function will operate on the symbolic link itself instead
        of its target; defaults to false
    :type nofollow: boolean, optional
    :return: list of tuples (name, value); note that if a namespace
       argument was passed, it (and the separator) will be stripped from
       the names returned
    :rtype: list
    :raises EnvironmentError: caused by any system errors
    
    .. note:: Since reading the whole attribute list is not an atomic
       operation, it might be possible that attributes are added
       or removed between the initial query and the actual reading
       of the attributes; the returned list will contain only the
       attributes that were present at the initial listing of the
       attribute names and that were still present when the read
       attempt for the value is made.
    .. versionadded:: 0.4
    .. versionchanged:: 0.5.1
       The namespace argument, if passed, cannot be None anymore; to
       explicitly specify an empty namespace, pass an empty
       string (byte string under Python 3).
    """
    pass

def list(item, nofollow=False, namespace=None): # real signature unknown; restored from __doc__
    """
    list(item[, nofollow=False, namespace=None])
    Return the list of attribute names for a file.
    
    Example:
    
        >>> xattr.list('/path/to/file')
        ['user.test', 'user.comment', 'system.posix_acl_access']
        >>> xattr.list('/path/to/file', namespace=xattr.NS_USER)
        ['test', 'comment']
    
    :param item: a string representing a file-name, or a file-like
        object, or a file descriptor; this represents the file on 
        which to act
    :param nofollow: if true and if
        the file name given is a symbolic link, the
        function will operate on the symbolic link itself instead
        of its target; defaults to false
    :type nofollow: boolean, optional
    :param namespace: if given, the attribute must not contain the
        namespace, but instead it will be taken from this parameter
    :type namespace: bytes
    :returns: the list of attributes; note that if a namespace 
        argument was passed, it (and the separator) will be stripped
        from the names
        returned
    :rtype: list
    :raises EnvironmentError: caused by any system errors
    
    .. versionadded:: 0.4
    .. versionchanged:: 0.5.1
       The namespace argument, if passed, cannot be None anymore; to
       explicitly specify an empty namespace, pass an empty
       string (byte string under Python 3).
    """
    pass

def listxattr(item, nofollow=False): # real signature unknown; restored from __doc__
    """
    listxattr(item[, nofollow=False])
    Return the list of attribute names for a file (deprecated).
    
    :param item: a string representing a file-name, or a file-like
        object, or a file descriptor; this represents the file on 
        which to act
    :param nofollow: if true and if
        the file name given is a symbolic link, the
        function will operate on the symbolic link itself instead
        of its target; defaults to false
    :type nofollow: boolean, optional
    
    .. deprecated:: 0.4
       this function has been deprecated by the :func:`list` function.
    """
    pass

def remove(item, name, nofollow=False, namespace=None): # real signature unknown; restored from __doc__
    """
    remove(item, name[, nofollow=False, namespace=None])
    Remove an attribute from a file.
    
    Example:
    
        >>> xattr.remove('/path/to/file', 'user.comment')
    
    :param item: a string representing a file-name, or a file-like
        object, or a file descriptor; this represents the file on 
        which to act
    :param string name: the attribute to remove;
        usually in the form of ``system.posix_acl`` or 
        ``user.mime_type``
    :param nofollow: if true and if
        the file name given is a symbolic link, the
        function will operate on the symbolic link itself instead
        of its target; defaults to false
    :type nofollow: boolean, optional
    :param namespace: if given, the attribute must not contain the
        namespace, but instead it will be taken from this parameter
    :type namespace: bytes
    :returns: None
    :raises EnvironmentError: caused by any system errors
    
    .. versionadded:: 0.4
    .. versionchanged:: 0.5.1
       The namespace argument, if passed, cannot be None anymore; to
       explicitly specify an empty namespace, pass an empty
       string (byte string under Python 3).
    """
    pass

def removexattr(item, name, nofollow=None): # real signature unknown; restored from __doc__
    """
    removexattr(item, name[, nofollow])
    Remove an attribute from a file (deprecated).
    
    :param item: a string representing a file-name, or a file-like
        object, or a file descriptor; this represents the file on 
        which to act
    :param string name: the attribute to remove;
        usually in the form of ``system.posix_acl`` or 
        ``user.mime_type``
    :param nofollow: if true and if
        the file name given is a symbolic link, the
        function will operate on the symbolic link itself instead
        of its target; defaults to false
    :type nofollow: boolean, optional
    
    .. deprecated:: 0.4
       this function has been deprecated by the :func:`remove` function.
    """
    pass

def set(item, name, value, flags=0, namespace=None): # real signature unknown; restored from __doc__
    """
    set(item, name, value[, flags=0, namespace=None])
    Set the value of a given extended attribute.
    
    Example:
    
        >>> xattr.set('/path/to/file', 'user.comment', 'test')
        >>> xattr.set('/path/to/file', 'comment', 'test', namespace=xattr.NS_USER)
    
    :param item: a string representing a file-name, or a file-like
        object, or a file descriptor; this represents the file on 
        which to act
    :param string name: the attribute whose value to set;
        usually in the form of ``system.posix_acl`` or ``user.mime_type``
    :param string value: possibly with embedded NULLs; note that there
        are restrictions regarding the size of the value, for
        example, for ext2/ext3, maximum size is the block size
    :param flags: if 0 or omitted the attribute will be
        created or replaced; if :const:`XATTR_CREATE`, the attribute
        will be created, giving an error if it already exists;
        if :const:`XATTR_REPLACE`, the attribute will be replaced,
        giving an error if it doesn't exist;
    :type flags: integer
    :param nofollow: if true and if
        the file name given is a symbolic link, the
        function will operate on the symbolic link itself instead
        of its target; defaults to false
    :type nofollow: boolean, optional
    :param namespace: if given, the attribute must not contain the
        namespace, but instead it will be taken from this parameter
    :type namespace: bytes
    :returns: None
    :raises EnvironmentError: caused by any system errors
    
    .. versionadded:: 0.4
    .. versionchanged:: 0.5.1
       The namespace argument, if passed, cannot be None anymore; to
       explicitly specify an empty namespace, pass an empty
       string (byte string under Python 3).
    """
    pass

def setxattr(item, name, value, flags=0, nofollow=False): # real signature unknown; restored from __doc__
    """
    setxattr(item, name, value[, flags=0, nofollow=False])
    Set the value of a given extended attribute (deprecated).
    
    Be careful in case you want to set attributes on symbolic
    links, you have to use all the 5 parameters; use 0 for the 
    flags value if you want the default behaviour (create or replace)
    
    :param item: a string representing a file-name, or a file-like
        object, or a file descriptor; this represents the file on 
        which to act
    :param string name: the attribute whose value to set;
        usually in the form of ``system.posix_acl`` or ``user.mime_type``
    :param string value: possibly with embedded NULLs; note that there
        are restrictions regarding the size of the value, for
        example, for ext2/ext3, maximum size is the block size
    :param flags: if 0 or omitted the attribute will be
        created or replaced; if :const:`XATTR_CREATE`, the attribute
        will be created, giving an error if it already exists;
        if :const:`XATTR_REPLACE`, the attribute will be replaced,
        giving an error if it doesn't exist;
    :type flags: integer
    :param nofollow: if true and if
        the file name given is a symbolic link, the
        function will operate on the symbolic link itself instead
        of its target; defaults to false
    :type nofollow: boolean, optional
    
    .. deprecated:: 0.4
       this function has been deprecated
       by the :func:`set` function.
    """
    pass

# no classes
