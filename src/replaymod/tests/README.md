## Run nosetests
```
(venv) replaymod $ nose2 -v
```

## Run pytests

[https://docs.pytest.org/en/8.0.x/example/markers.html] (markers)
https://pytest-with-eric.com/pytest-best-practices/pytest-setup-teardown/
https://pytest-with-eric.com/pytest-advanced/pytest-addoption/

PyTest Running Database Access
==============================

(venv) replaymod $ pwd
/Users/racheldaloia/sandbox/pyreplay/src/replaymod

(venv) replaymod $ pytest -v -m database_access
==================================================================== test session starts ====================================================================
platform darwin -- Python 3.11.4, pytest-8.0.0, pluggy-1.4.0 -- /Users/racheldaloia/sandbox/pyreplay/src/venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/racheldaloia/sandbox/pyreplay/src/replaymod
configfile: pytest.ini
collected 5 items / 5 deselected / 0 selected                                                                                                               

=================================================================== 5 deselected in 0.03s ===================================================================
(venv) Rachels-MacBook-Pro:replaymod racheldaloia$


PyTest Running WebTest
======================

(venv) replaymod $ pytest -v -m webtest
==================================================================== test session starts ====================================================================
platform darwin -- Python 3.11.4, pytest-8.0.0, pluggy-1.4.0 -- /Users/racheldaloia/sandbox/pyreplay/src/venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/racheldaloia/sandbox/pyreplay/src/replaymod
configfile: pytest.ini
collected 6 items / 5 deselected / 1 selected                                                                                                               

tests/test_cars.py::test_web_framework FAILED                                                                                                         [100%]

========================================================================= FAILURES ==========================================================================
____________________________________________________________________ test_web_framework _____________________________________________________________________

setup_data = 'Engine Started'

    @pytest.mark.webtest
    def test_web_framework(setup_data):
        response = 200
>       assert response == 404
E       assert 200 == 404

tests/test_cars.py:60: AssertionError
------------------------------------------------------------------- Captured stdout setup -------------------------------------------------------------------

Setting up engine...
Starting Up V6 engine...
Engine startup successful
continue...
----------------------------------------------------------------- Captured stdout teardown ------------------------------------------------------------------

Tearing down resources...
================================================================== short test summary info ==================================================================
FAILED tests/test_cars.py::test_web_framework - assert 200 == 404
============================================================== 1 failed, 5 deselected in 0.13s ==============================================================
(venv) replaymod $ 


Python Running WebTest 2.0
==========================

(venv) replaymod $ pytest -v -m webtest
==================================================================== test session starts ====================================================================
platform darwin -- Python 3.11.4, pytest-8.0.0, pluggy-1.4.0 -- /Users/racheldaloia/sandbox/pyreplay/src/venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/racheldaloia/sandbox/pyreplay/src/replaymod
configfile: pytest.ini
collected 6 items / 5 deselected / 1 selected                                                                                                               

tests/test_cars.py::test_web_framework FAILED                                                                                                         [100%]

========================================================================= FAILURES ==========================================================================
____________________________________________________________________ test_web_framework _____________________________________________________________________

setup_data = 'Engine Started'

    @pytest.mark.webtest
    def test_web_framework(setup_data):
        # answer = calculate_startup(setup_data)
        # assert answer == False
        # print("*******************************")
        # if answer:
        if setup_data == 'Engine Started':
            response = 200
>           assert response == 404
E           assert 200 == 404

tests/test_cars.py:68: AssertionError
------------------------------------------------------------------- Captured stdout setup -------------------------------------------------------------------

Setting up engine...
Starting Up V6 engine...
Engine startup successful
continue...
----------------------------------------------------------------- Captured stdout teardown ------------------------------------------------------------------

Tearing down resources...
================================================================== short test summary info ==================================================================
FAILED tests/test_cars.py::test_web_framework - assert 200 == 404
============================================================== 1 failed, 5 deselected in 0.13s ==============================================================
(venv) replaymod $ 


Python Running Specific TestSuite from test file
================================================

(venv) replaymod $ pytest -v tests/test_cars.py::TestCarSuite
==================================================================== test session starts ====================================================================
platform darwin -- Python 3.11.4, pytest-8.0.0, pluggy-1.4.0 -- /Users/racheldaloia/sandbox/pyreplay/src/venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/racheldaloia/sandbox/pyreplay/src/replaymod
configfile: pytest.ini
collected 4 items                                                                                                                                           

tests/test_cars.py::TestCarSuite::test_database_access PASSED                                                                                         [ 25%]
tests/test_cars.py::TestCarSuite::test_car_creation_for_brands[] PASSED                                                                               [ 50%]
tests/test_cars.py::TestCarSuite::test_car_creation_for_brands[BMW] PASSED                                                                            [ 75%]
tests/test_cars.py::TestCarSuite::test_car_creation_for_brands[Mercedes] FAILED                                                                       [100%]


Python Running Tests based on name search
=========================================

(venv) replaymod $ pytest -v -k brands
==================================================================== test session starts ====================================================================
platform darwin -- Python 3.11.4, pytest-8.0.0, pluggy-1.4.0 -- /Users/racheldaloia/sandbox/pyreplay/src/venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/racheldaloia/sandbox/pyreplay/src/replaymod
configfile: pytest.ini
collected 16 items / 13 deselected / 3 selected                                                                                                             

tests/test_cars.py::TestCarSuite::test_car_creation_for_brands[] PASSED                                                                               [ 33%]
tests/test_cars.py::TestCarSuite::test_car_creation_for_brands[BMW] PASSED                                                                            [ 66%]
tests/test_cars.py::TestCarSuite::test_car_creation_for_brands[Mercedes] FAILED                                                                       [100%]


