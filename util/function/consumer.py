from abc import ABC, abstractmethod

class Consumer(ABC):
    @abstractmethod
    def accept(self, t):
        ...
    
    def and_then(self, after):
        assert after is not None
        def f(t):
            self.accept(t)
            after.accept(t)
        return f