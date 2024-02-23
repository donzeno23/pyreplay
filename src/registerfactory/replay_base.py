from abc import ABCMeta, abstractmethod
from typing import Union

class ReplayExecutorBase(metaclass=ABCMeta):
    """ Base class for a replay """

    def __init__(self, **kwargs):
        """ Constructor """
        pass

    @abstractmethod
    def run(self, command: str) -> Union[str, str]:
        """ Abstract method to run a command """
        pass


    @abstractmethod
    def download(self, source: str) -> str:
        """ Abstract method to download a file """
        pass
