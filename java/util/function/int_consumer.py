from abc import ABC, abstractmethod

class IntConsumer(ABC):
    @abstractmethod
    def accept(self, value):
        ...
    
    def and_then(self, after):
        assert after is not None
        def f(t):
            self.accept(t)
            after.accept(t)
        return f