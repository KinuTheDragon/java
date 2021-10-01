from abc import ABC, abstractmethod

from java.util.function.int_consumer import IntConsumer

class Spliterator(ABC):
    @abstractmethod
    def try_advance(self, action):
        ...
    
    def for_each_remaining(self, action):
        while True:
            should_end = not self.try_advance(action)
            if should_end:
                break
    
    @abstractmethod
    def try_split(self):
        ...
    
    @abstractmethod
    def estimate_size(self):
        ...
    
    def get_exact_size_if_known(self):
        return self.estimate_size() if \
         self.characteristics() & self.SIZED \
         else -1
    
    @abstractmethod
    def characteristics(self):
        ...
    
    def has_characteristics(self, characteristics):
        return (self.characteristics() & characteristics) \
            == characteristics
    
    def get_comparator(self):
        raise RuntimeError
    
    ORDERED    = 0x00000010
    DISTINCT   = 0x00000001
    SORTED     = 0x00000004
    SIZED      = 0x00000040
    NONNULL    = 0x00000100
    IMMUTABLE  = 0x00000400
    CONCURRENT = 0x00001000
    SUBSIZED   = 0x00004000

    class OfPrimitive(ABC):
        pass
    
    class OfInt(ABC, OfPrimitive):
        def try_advance(self, action):
            if isinstance(action, IntConsumer):
                return super().try_advance(action)
            else:
                

Spliterator.OfPrimitive.__bases__ = ABC, Spliterator