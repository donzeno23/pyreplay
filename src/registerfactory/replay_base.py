from abc import ABCMeta, abstractmethod
from typing import Union
import polars as pl

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


class Executor(ReplayExecutorBase):
    def run(self):
        print("DEBUG: replay_base.run: executing log replay.")
        return("executing log replay...")
    
    def download(self):
        print("DEBUG: replay_base:download: downloading log.")
        return("downloading log...")
    
class ReplayRFB(metaclass=ABCMeta):

    @abstractmethod
    def rfb_check(self) -> None:
        """ Abstract method for executing ready for business checks """
        pass

class ReplayLogFetcher(metaclass=ABCMeta):

    @abstractmethod
    def get_log_file(self, type: str, source: str) -> str:
        """ Abstract method to get logs """
        pass


class LogFetcher(ReplayLogFetcher):

    def get_log_file(self, type: str, source: str) -> pl.DataFrame: 
        print("DEBUG: replay_base:get_log_file: getting log...")
        df = pl.DataFrame()
        return df


class ReplayMessage(metaclass=ABCMeta):

    @abstractmethod
    def extract_message(self, format: str, msgtype: str, filter: str) -> str:
        # TODO: see how serializer was done
        pass

    @abstractmethod
    def enhance_message(self, field: str) -> None:
        pass

    @abstractmethod
    def publish_message(self, type: str) -> None:
        pass


class ReplayReportGenerator(metaclass=ABCMeta):

    @abstractmethod
    def generate_report(self) -> None:
        pass

    @abstractmethod
    def validate_report(self) -> str:
        pass


class ReportGenerator(ReplayReportGenerator):

    def generate_report(self):
        print("DEBUG: replay_base:generate_report: running report generator")

    def validate_report(self):
        print("DEBUG: replay_base:validate_report: validating report")



