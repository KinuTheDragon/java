from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        ...
    
    @abstractmethod
    def next(self):
        ...
    
    def remove(self):
        raise NotImplementedError("remove")
    
    def for_each_remaining(self, action):
        asssert action is not None
        while self.has_next():
            action.accept(self.next())