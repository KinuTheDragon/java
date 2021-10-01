from abc import ABC, abstractmethod

class Supplier(ABC):
    @abstractmethod
    def get(self):
        ...