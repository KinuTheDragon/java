from abc import ABC, abstractmethod

class AutoCloseable(ABC):
    @abstractmethod
    def close(self):
        ...