import pytest

from context import registerfactory

from registerfactory.replay_factory import ReplayExecutorFactory
from apps.app_facade import AppReplayFacade

@pytest.fixture
def setup_replay():
    print("\n setup replay - build Facade...")
    app_replay_facade = AppReplayFacade()

    yield app_replay_facade



class TestAppReplay:

    # app_replay_facade = AppReplayFacade()

    @pytest.mark.env("stage1")
    def test_replay(self, setup_replay):
        # started = self.app_replay_facade.start()
        started = setup_replay.start()
        print(f"started: {started}")