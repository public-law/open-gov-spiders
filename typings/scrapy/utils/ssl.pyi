"""
This type stub file was generated by pyright.
"""

import OpenSSL._util as pyOpenSSLutil

SSL_OP_NO_TLSv1_3 = getattr(pyOpenSSLutil.lib, 'SSL_OP_NO_TLSv1_3', 0)
def ffi_buf_to_string(buf):
    ...

def x509name_to_string(x509name):
    ...

def get_temp_key_info(ssl_object):
    ...

def get_openssl_version():
    ...

