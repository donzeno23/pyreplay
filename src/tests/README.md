# Run tests
```
().venv) src % pytest -vrP tests
================================================================================= test session starts =================================================================================
platform darwin -- Python 3.11.7, pytest-8.0.0, pluggy-1.4.0 -- /Users/mdaloia/Documents/GitHub/pyreplay/src/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /Users/mdaloia/Documents/GitHub/pyreplay/src
configfile: pytest.ini
collected 4 items                                                                                                                                                                     

tests/test_replay_factory.py::test_with_fixture PASSED                                                                                                                          [ 25%]
tests/test_replay_factory.py::test_remote_service PASSED                                                                                                                        [ 50%]
tests/test_replay_factory.py::test_memory_service SKIPPED (JIRA: Advanced Operations issues - skipping!)                                                                        [ 75%]
tests/test_replay_factory.py::test_db_service SKIPPED (test requires env in ['stage1'])                                                                                         [100%]

======================================================================================= PASSES ========================================================================================
_________________________________________________________________________________ test_remote_service _________________________________________________________________________________
-------------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------------
logging message this is a test to medium REMOTE_SERVICE
============================================================================ 2 passed, 2 skipped in 0.01s =============================================================================
```