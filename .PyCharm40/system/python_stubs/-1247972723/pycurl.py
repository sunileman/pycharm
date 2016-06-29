# encoding: utf-8
# module pycurl
# from /usr/lib64/python2.7/site-packages/pycurl.so
# by generator 1.136
"""
This module implements an interface to the cURL library.

Types:

Curl() -> New object.  Create a new curl object.
CurlMulti() -> New object.  Create a new curl multi-object.

Functions:

global_init(option) -> None.  Initialize curl environment.
global_cleanup() -> None.  Cleanup curl environment.
version_info() -> tuple.  Return version information.
"""
# no imports

# Variables with simple values

ADDRESS_SCOPE = 171

APPCONNECT_TIME = 3145761

AUTOREFERER = 58

BUFFERSIZE = 98

CAINFO = 10065
CAPATH = 10097

COMPILE_DATE = 'Jun 10 2014 08:56:01'

COMPILE_LIBCURL_VERSION_NUM = 466176

COMPILE_PY_VERSION_HEX = 34014704

CONNECTTIMEOUT = 78

CONNECTTIMEOUT_MS = 156

CONNECT_ONLY = 141
CONNECT_TIME = 3145733

CONTENT_LENGTH_DOWNLOAD = 3145743
CONTENT_LENGTH_UPLOAD = 3145744

CONTENT_TYPE = 1048594

COOKIE = 10022
COOKIEFILE = 10031
COOKIEJAR = 10082
COOKIELIST = 10135
COPYPOSTFIELDS = 10165

CRLF = 27
CRLFILE = 10169

CSELECT_ERR = 4
CSELECT_IN = 1
CSELECT_OUT = 2

CURL_HTTP_VERSION_1_0 = 1
CURL_HTTP_VERSION_1_1 = 2

CURL_HTTP_VERSION_LAST = 3
CURL_HTTP_VERSION_NONE = 0

CUSTOMREQUEST = 10036

DEBUGFUNCTION = 20094

DNS_CACHE_TIMEOUT = 92

DNS_USE_GLOBAL_CACHE = 91

EFFECTIVE_URL = 1048577

EGDSOCKET = 10077

ENCODING = 10102

E_ABORTED_BY_CALLBACK = 42

E_BAD_CONTENT_ENCODING = 61

E_BAD_DOWNLOAD_RESUME = 36

E_BAD_FUNCTION_ARGUMENT = 43

E_CALL_MULTI_PERFORM = -1

E_CONV_FAILED = 75
E_CONV_REQD = 76

E_COULDNT_CONNECT = 7

E_COULDNT_RESOLVE_HOST = 6
E_COULDNT_RESOLVE_PROXY = 5

E_FAILED_INIT = 2

E_FILESIZE_EXCEEDED = 63

E_FILE_COULDNT_READ_FILE = 37

E_FTP_ACCESS_DENIED = 9

E_FTP_CANT_GET_HOST = 15

E_FTP_CANT_RECONNECT = 16

E_FTP_COULDNT_GET_SIZE = 32

E_FTP_COULDNT_RETR_FILE = 19

E_FTP_COULDNT_SET_ASCII = 29
E_FTP_COULDNT_SET_BINARY = 17

E_FTP_COULDNT_STOR_FILE = 25

E_FTP_COULDNT_USE_REST = 31

E_FTP_PORT_FAILED = 30

E_FTP_QUOTE_ERROR = 21

E_FTP_SSL_FAILED = 64

E_FTP_WEIRD_227_FORMAT = 14

E_FTP_WEIRD_PASS_REPLY = 11

E_FTP_WEIRD_PASV_REPLY = 13

E_FTP_WEIRD_SERVER_REPLY = 8

E_FTP_WEIRD_USER_REPLY = 12

E_FTP_WRITE_ERROR = 20

E_FUNCTION_NOT_FOUND = 41

E_GOT_NOTHING = 52

E_HTTP_POST_ERROR = 34

E_HTTP_RANGE_ERROR = 33

E_HTTP_RETURNED_ERROR = 22

E_INTERFACE_FAILED = 45

E_LDAP_CANNOT_BIND = 38

E_LDAP_INVALID_URL = 62

E_LDAP_SEARCH_FAILED = 39

E_LIBRARY_NOT_FOUND = 40

E_LOGIN_DENIED = 67

E_MULTI_BAD_EASY_HANDLE = 2

E_MULTI_BAD_HANDLE = 1

E_MULTI_INTERNAL_ERROR = 4

E_MULTI_OK = 0

E_MULTI_OUT_OF_MEMORY = 3

E_OK = 0

E_OPERATION_TIMEOUTED = 28

E_OUT_OF_MEMORY = 27

E_PARTIAL_FILE = 18

E_READ_ERROR = 26

E_RECV_ERROR = 56

E_REMOTE_FILE_NOT_FOUND = 78

E_SEND_ERROR = 55

E_SEND_FAIL_REWIND = 65

E_SHARE_IN_USE = 57

E_SSH = 79

E_SSL_CACERT = 60

E_SSL_CACERT_BADFILE = 77

E_SSL_CERTPROBLEM = 58
E_SSL_CIPHER = 59

E_SSL_CONNECT_ERROR = 35

E_SSL_ENGINE_INITFAILED = 66
E_SSL_ENGINE_NOTFOUND = 53
E_SSL_ENGINE_SETFAILED = 54

E_SSL_PEER_CERTIFICATE = 51

E_SSL_SHUTDOWN_FAILED = 80

E_TELNET_OPTION_SYNTAX = 49

E_TFTP_DISKFULL = 70
E_TFTP_EXISTS = 73
E_TFTP_ILLEGAL = 71
E_TFTP_NOSUCHUSER = 74
E_TFTP_NOTFOUND = 68
E_TFTP_PERM = 69
E_TFTP_UNKNOWNID = 72

E_TOO_MANY_REDIRECTS = 47

E_UNKNOWN_TELNET_OPTION = 48

E_UNSUPPORTED_PROTOCOL = 1

E_URL_MALFORMAT = 3

E_WRITE_ERROR = 23

FAILONERROR = 45

FILE = 10001

FOLLOWLOCATION = 52

FORBID_REUSE = 75

FORM_CONTENTS = 4
FORM_CONTENTTYPE = 14
FORM_FILE = 10
FORM_FILENAME = 16

FRESH_CONNECT = 74

FTPAPPEND = 50

FTPAUTH_DEFAULT = 0
FTPAUTH_SSL = 1
FTPAUTH_TLS = 2

FTPLISTONLY = 48

FTPMETHOD_DEFAULT = 0
FTPMETHOD_MULTICWD = 1
FTPMETHOD_NOCWD = 2
FTPMETHOD_SINGLECWD = 3

FTPPORT = 10017
FTPSSLAUTH = 129

FTPSSL_ALL = 3
FTPSSL_CONTROL = 2
FTPSSL_NONE = 0
FTPSSL_TRY = 1

FTP_ACCOUNT = 10134

FTP_ALTERNATIVE_TO_USER = 10147

FTP_CREATE_MISSING_DIRS = 110

FTP_ENTRY_PATH = 1048606

FTP_FILEMETHOD = 138

FTP_RESPONSE_TIMEOUT = 112

FTP_SKIP_PASV_IP = 137

FTP_SSL = 119

FTP_SSL_CCC = 154

FTP_USE_EPRT = 106
FTP_USE_EPSV = 85

GLOBAL_ACK_EINTR = 4

GLOBAL_ALL = 3
GLOBAL_DEFAULT = 3
GLOBAL_NOTHING = 0
GLOBAL_SSL = 1
GLOBAL_WIN32 = 2

HEADER = 42
HEADERFUNCTION = 20079

HEADER_SIZE = 2097163

HTTP200ALIASES = 10104
HTTPAUTH = 107

HTTPAUTH_ANY = -17
HTTPAUTH_ANYSAFE = -18
HTTPAUTH_AVAIL = 2097175
HTTPAUTH_BASIC = 1
HTTPAUTH_DIGEST = 2
HTTPAUTH_GSSNEGOTIATE = 4
HTTPAUTH_NONE = 0
HTTPAUTH_NTLM = 8

HTTPGET = 80
HTTPHEADER = 10023
HTTPPOST = 10024
HTTPPROXYTUNNEL = 61

HTTP_CODE = 2097154
HTTP_CONNECTCODE = 2097174

HTTP_CONTENT_DECODING = 158

HTTP_TRANSFER_DECODING = 157

HTTP_VERSION = 84

IGNORE_CONTENT_LENGTH = 136

INFILE = 10009
INFILESIZE = 30115

INFILESIZE_LARGE = 30115

INFOTYPE_DATA_IN = 3
INFOTYPE_DATA_OUT = 4

INFOTYPE_HEADER_IN = 1
INFOTYPE_HEADER_OUT = 2

INFOTYPE_SSL_DATA_IN = 5
INFOTYPE_SSL_DATA_OUT = 6

INFOTYPE_TEXT = 0

INFO_COOKIELIST = 4194332
INFO_FILETIME = 2097166

INTERFACE = 10062

IOCMD_NOP = 0
IOCMD_RESTARTREAD = 1

IOCTLDATA = 10131
IOCTLFUNCTION = 20130

IOE_FAILRESTART = 2
IOE_OK = 0
IOE_UNKNOWNCMD = 1

IPRESOLVE = 113

IPRESOLVE_V4 = 1
IPRESOLVE_V6 = 2
IPRESOLVE_WHATEVER = 0

ISSUERCERT = 10170

KRB4LEVEL = 10063

LASTSOCKET = 2097181

LOCALPORT = 139
LOCALPORTRANGE = 140

LOCK_DATA_COOKIE = 2
LOCK_DATA_DNS = 3

LOW_SPEED_LIMIT = 19
LOW_SPEED_TIME = 20

MAXCONNECTS = 71
MAXFILESIZE = 30117

MAXFILESIZE_LARGE = 30117

MAXREDIRS = 68

MAX_RECV_SPEED_LARGE = 30146

MAX_SEND_SPEED_LARGE = 30145

M_MAXCONNECTS = 6
M_PIPELINING = 3
M_SOCKETFUNCTION = 20001
M_TIMERFUNCTION = 20004

NAMELOOKUP_TIME = 3145732

NETRC = 51

NETRC_FILE = 10118
NETRC_IGNORED = 0
NETRC_OPTIONAL = 1
NETRC_REQUIRED = 2

NEW_DIRECTORY_PERMS = 160

NEW_FILE_PERMS = 159

NOBODY = 44
NOPROGRESS = 43
NOSIGNAL = 99

NUM_CONNECTS = 2097178

OPENSOCKETFUNCTION = 20163

OPT_FILETIME = 69

OS_ERRNO = 2097177

POLL_IN = 1
POLL_INOUT = 3
POLL_NONE = 0
POLL_OUT = 2
POLL_REMOVE = 4

PORT = 3
POST = 47
POST301 = 161
POSTFIELDS = 10015
POSTFIELDSIZE = 30120

POSTFIELDSIZE_LARGE = 30120

POSTQUOTE = 10039

PREQUOTE = 10093

PRETRANSFER_TIME = 3145734

PRIMARY_IP = 1048608

PROGRESSFUNCTION = 20056
PROXY = 10004
PROXYAUTH = 111

PROXYAUTH_AVAIL = 2097176

PROXYPORT = 59
PROXYTYPE = 101

PROXYTYPE_HTTP = 0
PROXYTYPE_SOCKS4 = 4
PROXYTYPE_SOCKS5 = 5

PROXYUSERPWD = 10006

PROXY_TRANSFER_MODE = 166

PUT = 54

QUOTE = 10028

RANDOM_FILE = 10076

RANGE = 10007

READDATA = 10009
READFUNCTION = 20012

READFUNC_ABORT = 268435456

REDIRECT_COUNT = 2097172
REDIRECT_TIME = 3145747
REDIRECT_URL = 1048607

REFERER = 10016

REQUEST_SIZE = 2097164

RESPONSE_CODE = 2097154

RESUME_FROM = 30116

RESUME_FROM_LARGE = 30116

SHARE = 10100
SH_SHARE = 1
SH_UNSHARE = 2

SIZE_DOWNLOAD = 3145736
SIZE_UPLOAD = 3145735

SOCKET_TIMEOUT = -1

SPEED_DOWNLOAD = 3145737
SPEED_UPLOAD = 3145738

SSH_AUTH_ANY = -1
SSH_AUTH_DEFAULT = -1
SSH_AUTH_HOST = 4
SSH_AUTH_KEYBOARD = 8
SSH_AUTH_NONE = 0
SSH_AUTH_PASSWORD = 2
SSH_AUTH_PUBLICKEY = 1
SSH_AUTH_TYPES = 151

SSH_HOST_PUBLIC_KEY_MD5 = 10162

SSH_PRIVATE_KEYFILE = 10153

SSH_PUBLIC_KEYFILE = 10152

SSLCERT = 10025
SSLCERTPASSWD = 10026
SSLCERTTYPE = 10086
SSLENGINE = 10089

SSLENGINE_DEFAULT = 90

SSLKEY = 10087
SSLKEYPASSWD = 10026
SSLKEYTYPE = 10088
SSLVERSION = 32

SSLVERSION_DEFAULT = 0
SSLVERSION_SSLv2 = 2
SSLVERSION_SSLv3 = 3
SSLVERSION_TLSv1 = 1

SSL_CIPHER_LIST = 10083

SSL_ENGINES = 4194331

SSL_SESSIONID_CACHE = 150

SSL_VERIFYHOST = 81
SSL_VERIFYPEER = 64
SSL_VERIFYRESULT = 2097165

STARTTRANSFER_TIME = 3145745

STDERR = 10037

TCP_NODELAY = 121

TIMECONDITION = 33

TIMECONDITION_IFMODSINCE = 1
TIMECONDITION_IFUNMODSINCE = 2
TIMECONDITION_LASTMOD = 3
TIMECONDITION_NONE = 0

TIMEOUT = 13

TIMEOUT_MS = 155

TIMEVALUE = 34

TOTAL_TIME = 3145731

TRANSFERTEXT = 53

UNRESTRICTED_AUTH = 105

UPLOAD = 46

URL = 10002

USERAGENT = 10018
USERPWD = 10005

VERBOSE = 41

version = 'libcurl/7.29.0 NSS/3.19.1 Basic ECC zlib/1.2.7 libidn/1.28 libssh2/1.4.3'

WRITEDATA = 10001
WRITEFUNCTION = 20011

WRITEFUNC_PAUSE = 268435457

WRITEHEADER = 10029

# functions

def Curl(): # real signature unknown; restored from __doc__
    """ Curl() -> New curl object.  Implicitly calls global_init() if not called. """
    pass

def CurlMulti(): # real signature unknown; restored from __doc__
    """ CurlMulti() -> New curl multi-object. """
    pass

def CurlShare(): # real signature unknown; restored from __doc__
    """ CurlShare() -> New CurlShare object. """
    pass

def global_cleanup(): # real signature unknown; restored from __doc__
    """ global_cleanup() -> None.  Cleanup curl environment. """
    pass

def global_init(option): # real signature unknown; restored from __doc__
    """ global_init(option) -> None.  Initialize curl environment. """
    pass

def version_info(): # real signature unknown; restored from __doc__
    """ version_info() -> tuple.  Returns a 12-tuple with the version info. """
    pass

# classes

class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



