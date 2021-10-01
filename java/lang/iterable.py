from abc import ABC, abstractmethod

from java.util.spliterators import Spliterators

class Iterable(ABC):
    @abstractmethod
    def iterator(self):
        ...
    
    __iter__ = iterator
    
    def for_each(self, action):
        assert action is not None
        for t in self:
            action.accept(t)
    
    def spliterator(self):
        return Spliterators.spliterator_unknown_size(self.iterator(), 0)