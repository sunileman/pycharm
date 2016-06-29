# encoding: utf-8
# module rpm._rpmb
# from /usr/lib64/python2.7/site-packages/rpm/_rpmb.so
# by generator 1.136
# no doc
# no imports

# Variables with simple values

RPMBUILD_BUILD = 2
RPMBUILD_CHECK = 8
RPMBUILD_CLEAN = 16
RPMBUILD_FILECHECK = 32
RPMBUILD_INSTALL = 4
RPMBUILD_ISICON = 4
RPMBUILD_ISNO = 8
RPMBUILD_ISPATCH = 2
RPMBUILD_ISSOURCE = 1
RPMBUILD_NONE = 0
RPMBUILD_PACKAGEBINARY = 128
RPMBUILD_PACKAGESOURCE = 64

RPMBUILD_PKG_NODIRTOKENS = 1
RPMBUILD_PKG_NONE = 0

RPMBUILD_PREP = 1
RPMBUILD_RMBUILD = 512
RPMBUILD_RMSOURCE = 256
RPMBUILD_RMSPEC = 2048

RPMSPEC_ANYARCH = 1
RPMSPEC_FORCE = 2
RPMSPEC_NOLANG = 4
RPMSPEC_NONE = 0

# no functions
# classes

class spec(object):
    """ RPM Spec file object """
    def _doBuild(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    build = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    check = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    clean = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    install = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    packages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sourceHeader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sources = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class specPkg(object):
    # no doc
    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



