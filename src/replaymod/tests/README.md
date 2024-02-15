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


## When test has stdin
```
OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.

(venv) Rachels-MacBook-Pro:replaymod racheldaloia$ pytest -v -s -E stage1
=========================================== test session starts ===========================================
platform darwin -- Python 3.11.4, pytest-8.0.0, pluggy-1.4.0 -- /Users/racheldaloia/sandbox/pyreplay/src/venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/racheldaloia/sandbox/pyreplay/src/replaymod
configfile: pytest.ini
collecting ... This was instantiated??
collected 16 items                                                                                        

tests/test_advanced.py::AdvancedTestSuite::test_thoughts FAILED
tests/test_basic.py::BasicTestSuite::test_absolute_truth_and_meaning PASSED
tests/test_cars.py::test_if_apple_is_evil PASSED
tests/test_cars.py::test_advanced_db_operation SKIPPED (JIRA: Advanced Operations issues - skip...)
tests/test_cars.py::test_basic_db_operation PASSED
tests/test_cars.py::test_custom_option Custom option value: default_value
PASSED
tests/test_cars.py::test_pass_gen FAILED
tests/test_cars.py::test_web_framework 
Setting up engine...
Starting Up V6 engine...
Engine startup successful
continue...
FAILED
Tearing down resources...

tests/test_cars.py::TestClass::test_startup PASSED
tests/test_cars.py::TestClass::test_startup_and_more PASSED
tests/test_cars.py::TestCarSuite::test_database_access PASSED
tests/test_cars.py::TestCarSuite::test_car_creation_for_brands[] SKIPPED (test requires env in ...)
tests/test_cars.py::TestCarSuite::test_car_creation_for_brands[BMW] SKIPPED (test requires env ...)
tests/test_cars.py::TestCarSuite::test_car_creation_for_brands[Mercedes] SKIPPED (test requires...)
tests/test_notification.py::NotificationTestSuite::test_absolute_truth_and_meaning PASSED
tests/test_notification.py::NotificationTestSuite::test_notification_factory Enter the provider (FastNotify or SendBlue): SendBlue
Formatting Email content
PASSED

================================================ FAILURES =================================================
_____________________________________ AdvancedTestSuite.test_thoughts _____________________________________

self = <test_advanced.AdvancedTestSuite testMethod=test_thoughts>

    def test_thoughts(self):
>       self.assertIsNone(replay.hmm())
E       AttributeError: module 'replay' has no attribute 'hmm'

tests/test_advanced.py:12: AttributeError
______________________________________________ test_pass_gen ______________________________________________

pass_gen = 'default_value'

    def test_pass_gen(pass_gen) -> None:
        custom_value = pass_gen
>       assert custom_value == 'me2'
E       AssertionError: assert 'default_value' == 'me2'
E         
E         - me2
E         + default_value

tests/test_cars.py:97: AssertionError
___________________________________________ test_web_framework ____________________________________________

setup_data = 'Engine Started'

    @pytest.mark.webtest
    def test_web_framework(setup_data) -> None:
        # answer = calculate_startup(setup_data)
        # assert answer == False
        # print("*******************************")
        # if answer:
        if setup_data == 'Engine Started':
            response = 200
>           assert response == 404
E           assert 200 == 404

tests/test_cars.py:112: AssertionError
========================================= short test summary info =========================================
FAILED tests/test_advanced.py::AdvancedTestSuite::test_thoughts - AttributeError: module 'replay' has no attribute 'hmm'
FAILED tests/test_cars.py::test_pass_gen - AssertionError: assert 'default_value' == 'me2'
FAILED tests/test_cars.py::test_web_framework - assert 200 == 404
================================= 3 failed, 9 passed, 4 skipped in 3.57s ==================================
(venv) Rachels-MacBook-Pro:replaymod racheldaloia$ 
```