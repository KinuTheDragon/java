from abc import ABC, abstractmethod

from java.lang.iterable import Iterable
from java.util.spliterators import Spliterators

class Collection(ABC, Iterable):
    @abstractmethod
    def size(self):
        ...
    
    @abstractmethod
    def is_empty(self):
        ...
    
    @abstractmethod
    def contains(self, o):
        ...
    
    @abstractmethod
    def iterator(self):
        ...
    
    __iter__ = iterator

    @abstractmethod
    def to_array(self, a = None):
        ...
    
    @abstractmethod
    def add(self, e):
        ...
    
    @abstractmethod
    def remove(self, o):
        ...
    
    @abstractmethod
    def contains_all(self, c):
        ...
    
    @abstractmethod
    def add_all(self, c):
        ...
    
    @abstractmethod
    def remove_all(self, c):
        ...
    
    def remove_if(self, filter):
        assert filter is not None
        removed = False
        each = self.iterator()
        while each.has_next():
            if 