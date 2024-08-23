'''
multiple inheritance is not for stacking functionality
but for type relations
inherit from multiple superclasses to be able
to check for types implemented
'''

from abc import ABC, abstractmethod

class Stream(ABC):
    @abstractmethod
    def receive(self):
        pass

    @abstractmethod
    def send(self, msg):
        pass

    @abstractmethod
    def close(self):
        pass

class Iterable(ABC):
    def __iter__(self):
        pass

class MessageStream(Stream, Iterable):
    def receive(self):
        pass

    def send(self, msg):
        pass

    def close(self):
        pass

    def __iter__(self):
        pass

m = MessageStream()
print(isinstance(m, Stream))
print(isinstance(m, Iterable))