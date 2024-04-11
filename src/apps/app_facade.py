from registerfactory.replay_base import Executor, LogFetcher, ReportGenerator
from registerfactory.replay_factory import ReplayExecutorFactory

@ReplayExecutorFactory.register("app.one")
class AppReplayFacade:
    """
    Represents a facade for various app replay components
    """
    def __init__(self):
        self.logfetcher = LogFetcher()
        self.executor = Executor()
        self.reportgen = ReportGenerator()

    def start(self):
        self.executor.run()
        df = self.logfetcher.get_log_file(type="binary", source="mongod")
        self.reportgen.generate_report()