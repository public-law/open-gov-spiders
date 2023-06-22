"""
This type stub file was generated by pyright.
"""

from typing import Optional, Type, TypeVar
from twisted.internet.defer import Deferred
from scrapy.http.request import Request
from scrapy.settings import BaseSettings
from scrapy.spiders import Spider

BaseDupeFilterTV = TypeVar("BaseDupeFilterTV", bound="BaseDupeFilter")
class BaseDupeFilter:
    @classmethod
    def from_settings(cls: Type[BaseDupeFilterTV], settings: BaseSettings) -> BaseDupeFilterTV:
        ...
    
    def request_seen(self, request: Request) -> bool:
        ...
    
    def open(self) -> Optional[Deferred]:
        ...
    
    def close(self, reason: str) -> Optional[Deferred]:
        ...
    
    def log(self, request: Request, spider: Spider) -> None:
        """Log that a request has been filtered"""
        ...
    


RFPDupeFilterTV = TypeVar("RFPDupeFilterTV", bound="RFPDupeFilter")
class RFPDupeFilter(BaseDupeFilter):
    """Request Fingerprint duplicates filter"""
    def __init__(self, path: Optional[str] = ..., debug: bool = ..., *, fingerprinter=...) -> None:
        ...
    
    @classmethod
    def from_settings(cls: Type[RFPDupeFilterTV], settings: BaseSettings, *, fingerprinter=...) -> RFPDupeFilterTV:
        ...
    
    @classmethod
    def from_crawler(cls, crawler): # -> Self@RFPDupeFilter:
        ...
    
    def request_seen(self, request: Request) -> bool:
        ...
    
    def request_fingerprint(self, request: Request) -> str:
        ...
    
    def close(self, reason: str) -> None:
        ...
    
    def log(self, request: Request, spider: Spider) -> None:
        ...
    


