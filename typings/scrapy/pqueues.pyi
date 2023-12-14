"""
This type stub file was generated by pyright.
"""

logger = ...
class ScrapyPriorityQueue:
    """A priority queue implemented using multiple internal queues (typically,
    FIFO queues). It uses one internal queue for each priority value. The internal
    queue must implement the following methods:

        * push(obj)
        * pop()
        * close()
        * __len__()

    Optionally, the queue could provide a ``peek`` method, that should return the
    next object to be returned by ``pop``, but without removing it from the queue.

    ``__init__`` method of ScrapyPriorityQueue receives a downstream_queue_cls
    argument, which is a class used to instantiate a new (internal) queue when
    a new priority is allocated.

    Only integer priorities should be used. Lower numbers are higher
    priorities.

    startprios is a sequence of priorities to start with. If the queue was
    previously closed leaving some priority buckets non-empty, those priorities
    should be passed in startprios.

    """
    @classmethod
    def from_crawler(cls, crawler, downstream_queue_cls, key, startprios=...): # -> Self:
        ...
    
    def __init__(self, crawler, downstream_queue_cls, key, startprios=...) -> None:
        ...
    
    def init_prios(self, startprios): # -> None:
        ...
    
    def qfactory(self, key):
        ...
    
    def priority(self, request):
        ...
    
    def push(self, request): # -> None:
        ...
    
    def pop(self): # -> None:
        ...
    
    def peek(self): # -> None:
        """Returns the next object to be returned by :meth:`pop`,
        but without removing it from the queue.

        Raises :exc:`NotImplementedError` if the underlying queue class does
        not implement a ``peek`` method, which is optional for queues.
        """
        ...
    
    def close(self): # -> list[Any]:
        ...
    
    def __len__(self): # -> int:
        ...
    


class DownloaderInterface:
    def __init__(self, crawler) -> None:
        ...
    
    def stats(self, possible_slots): # -> list[tuple[int, Any]]:
        ...
    
    def get_slot_key(self, request):
        ...
    


class DownloaderAwarePriorityQueue:
    """PriorityQueue which takes Downloader activity into account:
    domains (slots) with the least amount of active downloads are dequeued
    first.
    """
    @classmethod
    def from_crawler(cls, crawler, downstream_queue_cls, key, startprios=...): # -> Self:
        ...
    
    def __init__(self, crawler, downstream_queue_cls, key, slot_startprios=...) -> None:
        ...
    
    def pqfactory(self, slot, startprios=...): # -> ScrapyPriorityQueue:
        ...
    
    def pop(self): # -> None:
        ...
    
    def push(self, request): # -> None:
        ...
    
    def peek(self): # -> None:
        """Returns the next object to be returned by :meth:`pop`,
        but without removing it from the queue.

        Raises :exc:`NotImplementedError` if the underlying queue class does
        not implement a ``peek`` method, which is optional for queues.
        """
        ...
    
    def close(self): # -> dict[Any, Any]:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def __contains__(self, slot): # -> bool:
        ...
    


