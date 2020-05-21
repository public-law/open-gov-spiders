"""
This type stub file was generated by pyright.
"""

'''
$Id: tzfile.py,v 1.8 2004/06/03 00:15:24 zenzen Exp $
'''
def _byte_string(s):
    """Cast a string or byte string to an ASCII byte string."""
    ...

_NULL = _byte_string('\0')
def _std_string(s):
    """Cast a string or byte string to an ASCII string."""
    ...

def build_tzinfo(zone, fp):
    ...

if __name__ == '__main__':
    base = os.path.join(os.path.dirname(__file__), 'zoneinfo')
    tz = build_tzinfo('Australia/Melbourne', open(os.path.join(base, 'Australia', 'Melbourne'), 'rb'))
    tz = build_tzinfo('US/Eastern', open(os.path.join(base, 'US', 'Eastern'), 'rb'))
