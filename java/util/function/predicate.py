from abc import ABC, abstractmethod

class Predicate(ABC):
    def test(self, t):
        raise NotImplementedError
    
    def and_(self, other):
        assert other is not None
        p = self.__class__()
        p.test = lambda t: \
            self.test(t) and other.test(t)
        return p
    
    def negate(self):
        p = self.__class__()
        p.test = lambda t: not self.test(t)
        return p
    
    def or_(self, other):
        assert other is not None
        p = self.__class__()
        p.test = lambda t: \
            self.test(t) and other.test(t)
        return p
    
    @staticmethod
    def is_equal(target_ref):
        p = Predicate()
        if target_ref is None:
            p.test = lambda t: t is None
        else:
            p.test = lambda t: t == target_ref
        return p