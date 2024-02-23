import shlex
import subprocess

from typing import Union

from replay_base import ReplayExecutorBase
from replay_factory import ReplayExecutorFactory

@ReplayExecutorFactory.register('local')
class LocalReplayExecutor(ReplayExecutorBase):

    def run(self, command: str) -> Union[str, str]:
        """ Runs the given command using subprocess """

        args = shlex.split(command)
        stdout, stderr = subprocess.Popen(args,
                                          stdout=subprocess.PIPE,
                                          stderr=subprocess.PIPE).communicate()
        
        out = stdout.decode('utf-8')
        err = stderr.decode('utf-8')
        return out, err
    

    def download(self):
        raise NotImplementedError
    
    