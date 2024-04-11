from replay_base import Executor, LogFetcher, ReportGenerator
from replay_factory import ReplayExecutorFactory


class ReplayFacade:
    """
    Represents a facade for various replay parts
    """

    def __init__(self):
        self.executor = Executor()
        self.logfetcher = LogFetcher()
        self.reportgen = ReportGenerator()

    def start(self):
        self.executor.run()
        df = self.logfetcher.get_log_file(type="binary", source="mongo")
        print(f"Dataframe: {df.head()}")
        self.reportgen.generate_report()