"""
This type stub file was generated by pyright.
"""

from typing import Iterable, List, Optional, Tuple, Type, TypeVar, Union
from scrapy.http.request import Request
from scrapy.http.response.text import TextResponse

"""
This module implements the FormRequest class which is a more convenient class
(than Request) to generate Requests based on form data.

See documentation in docs/topics/request-response.rst
"""
FormRequestTypeVar = TypeVar("FormRequestTypeVar", bound="FormRequest")
FormdataKVType = Tuple[str, Union[str, Iterable[str]]]
FormdataType = Optional[Union[dict, List[FormdataKVType]]]
class FormRequest(Request):
    valid_form_methods = ...
    def __init__(self, *args, formdata: FormdataType = ..., **kwargs) -> None:
        ...
    
    @classmethod
    def from_response(cls: Type[FormRequestTypeVar], response: TextResponse, formname: Optional[str] = ..., formid: Optional[str] = ..., formnumber: int = ..., formdata: FormdataType = ..., clickdata: Optional[dict] = ..., dont_click: bool = ..., formxpath: Optional[str] = ..., formcss: Optional[str] = ..., **kwargs) -> FormRequestTypeVar:
        ...
    


