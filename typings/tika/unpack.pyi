"""
This type stub file was generated by pyright.
"""

_text_wrapper = ...
def from_file(filename, serverEndpoint=..., requestOptions=...): # -> dict[Unknown, Unknown]:
    '''
    Parse from file
    :param filename: file
    :param serverEndpoint: Tika server end point (optional)
    :return:
    '''
    ...

def from_buffer(string, serverEndpoint=..., requestOptions=...): # -> dict[Unknown, Unknown]:
    '''
    Parse from buffered content
    :param string:  buffered content
    :param serverEndpoint: Tika server URL (Optional)
    :return: parsed content
    '''
    ...

