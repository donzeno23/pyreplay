'''
We can define a common contract which all the storage implementations
follow and the Logger class just knows that it has to invoke that
contract to get that work done.
'''

from abc import ABC, abstractmethod

class ReplayOperations(ABC):

    @abstractmethod
    def log(self, message):
        print("logging has started...")
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def transfer(self):
        pass