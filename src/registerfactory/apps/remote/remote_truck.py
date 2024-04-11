from typing import Union

from replay_base import ReplayExecutorBase
from replay_factory import ReplayExecutorFactory

@ReplayExecutorFactory.register('remote.truck')
class RemoteTruckReplayExecutor(ReplayExecutorBase):
    # raise NotImplementedError
    # pass

    def __init__(self, **kwargs):
        """ Constructor """

        self._hostname = kwargs.get('hostname', 'localhost')
        self._username = kwargs.get('username', None)
        self._password = kwargs.get('password', None)
        self._pem = kwargs.get('pem', None)

    def run(self, command: str) -> Union[str, str]:
        """ Runs the command using paramiko """

        # Creates the client, connects and issues the command
        client = "Client 1"

        out = "Logged In!"
        err = ""

        return out, err
    

    def download(self, source=""):
        print(f"Downloading from {source}")
        return f"Downloading from {source}"
    

    def transform(self, message):
        print(f"Transforming message: {message}")
        return f"Transforming mesage: {message}"