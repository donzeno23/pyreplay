import pytest

from context import replayfactory

from replayfactory.replay_factory import ReplayFactory
from replayfactory.remote_service_replay_registration import RemoteServiceLog
from replayfactory.inmemory_replay_registration import InMemoryLog
from replayfactory.file_replay_registration import FileLog


replay = ReplayFactory()
remote_replay = RemoteServiceLog()
## remote_replay.register()
inmemory_replay = InMemoryLog()
file_replay = FileLog()

@pytest.fixture
def example_fixture():
    return 1


def test_with_fixture(example_fixture):
    assert example_fixture == 1

def test_remote_service_logging():
    output = remote_replay.log('this is a test of the logging remote service')
    assert output == 'REMOTE_LOGGING'

def test_remote_service_connect():
    output = remote_replay.connect()
    assert output == 'REMOTE_CONNECT'

def test_remote_service_transfer():
    output = remote_replay.transfer('this is a test of the transfer remote service')
    assert output == 'REMOTE_TRANSFER'

def test_memory_service():
    output = inmemory_replay.log('this is a test of in-memory')
    assert output == 'MEMORY'

# Note: Running with  "pytest -v -s -E staging" the below test will be skipped
@pytest.mark.env("stage1")
def test_db_service():
    # replay.log('this is a test of the database', 'DB')
    assert True

@pytest.mark.skip(reason="JIRA: File service not yet implemented!")
def test_file_service():
    # replay.log('this is a test of the file system', 'File')
    output = file_replay.log('testing 123!')
    assert True

def test_file_service_log():
    # replay.log('this is a test of the file system', 'File')
    output = file_replay.log('testing 123!')
    assert output == "FILE_LOG:log"


def test_file_service_transform():
    output = file_replay.transform('transform 123!')
    assert output == "transform 123!"