from abc import ABC, abstractmethod

from java.lang.auto_closeable import AutoCloseable

class BaseStream(ABC, AutoCloseable):
    @abstractmethod
    def iterator(self):
        ...
    
    __iter__ = iterator
    
    @abstractmethod
    def spliterator(self):
        ...
    
    @abstractmethod
    def is_parallel(self):
        ...
    
    @abstractmethod
    def sequential(self):
        ...
    
    @abstractmethod
    def parallel(self):
        ...
    
    @abstractmethod
    def unordered(self):
        ...
    
    @abstractmethod
    def on_close(self, close_handler):
        ...
    
    @abstractmethod
    def close(self):
        ...