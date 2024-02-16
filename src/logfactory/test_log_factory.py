import pytest

from logger_using_factory_with_class import LoggerFactory

logger = LoggerFactory()


@pytest.fixture
def example_fixture():
    return 1


def test_with_fixture(example_fixture):
    assert example_fixture == 1


def test_remote_service():
    logger.log('this is a test', 'REMOTE_SERVICE')
    assert False

@pytest.mark.skip(reason="JIRA: Advanced Operations issues - skipping!")
def test_memory_service():
    logger.log('this is a test', 'MEMORY')
    assert True

# Note: Running with  "pytest -v -s -E staging" the below test will be skipped
@pytest.mark.env("stage1")
def test_db_service():
    logger.log('this is a test', 'DB')
    assert True
    