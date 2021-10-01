from abc import ABC, abstractmethod

class AbstractCollection(ABC):
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def iterator(self):
        ...
    
    __iter__ = iterator
    
    @abstractmethod
    def size(self):
        ...
    
    def add(self, o):
        raise NotImplementedError
    
    def add_all(self, c):
        itr = c.iterator()
        modified = False
        pos = c.size()
        while True:
            pos -= 1
            if pos < 0: break
            modified = modified or self.add(itr.next())
        return modified
    
    def clear(self):
        itr = self.iterator()
        pos = self.size()
        while True:
            pos -= 1
            if pos < 0: break
            itr.next()
            itr.remove()
    
    def contains(self, o):
        itr = self.iterator()
        pos = self.size()
        while True:
            pos -= 1
            if pos < 0: break
            if o == itr.next():
                return True
        return False
    
    def contains_all(self, c):
        itr = c.iterator()
        pos = c.size()
        while True:
            pos -= 1
            if pos < 0: break
            if not self.contains(itr.next()):
                return False
        return True
    
    def is_empty(self):
        return self.size() == 0
    
    def remove(self, o):
        itr = self.iterator()
        pos = self.size()
        while True:
            pos -= 1
            if pos < 0: break
            if o == itr.next():
                itr.remove()
                return True
        return False
    
    def remove_all(self, c):
        return self.__remove_all_internal(c)
    
    def __remove_all_internal(self, c):
        itr = self.iterator()
        modified = False
        pos = self.size()
        while True:
            pos -= 1
            if pos < 0: break
            if c.contains(itr.next()):
                itr.remove()
                modified = True
        return modified
    
    def retain_all(self, c):
        return self.__retain_all_internal(c)
    
    def __retain_all_internal(self, c):
        itr = self.iterator()
        modified = False
        pos = self.size()
        while True:
            pos -= 1
            if pos < 0: break
            if not c.contains(itr.next()):
                itr.remove()
                modified = True
        return modified
    
    def to_array(self, a = None):
        size = self.size()
        if a is None:
            itr = self.iterator()
            a = [None] * size
        else:
            for i in range(len(a)):
                a[i] = None
            while len(a) < size:
                a.append(None)
            while len(a) > size:
                a.pop()
        for pos in range(size):
            a[pos] = itr.next()
        return a
    
    def to_string(self):
        itr = self.iterator()
        r = "["
        has_next = itr.has_next()
        while has_next:
            o = itr.next()
            if o is self:
                r += "<this>"
            else:
                r += str(o)
            has_next = itr.has_next()
            if has_next:
                r += ", "
        r += "]"
        return r
    
    __str__ = to_string
    
    @staticmethod
    def equals(o1, o2):
        return o1 is not None and o2 is not None and o1 == o2
    
    @staticmethod
    def hash_code(o):
        return 0 if o is None else hash(o)