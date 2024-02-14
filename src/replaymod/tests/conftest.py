import sys
import pytest

ALL = set("darwin linux win32".split())


def pytest_addoption(parser):
    parser.addoption("-E", dest="env", action="store", metavar="NAME",
        help="only run tests matching the environment NAME.")
    
    parser.addoption("--custom-option", action="store", default="default_value", 
        help="Description of the custom option.")


def pytest_configure(config):
    # register an additional marker
    config.addinivalue_line("markers",
        "env(name): mark test to run only on named environment")
    # if config.getoption('-E'):
    #     config.addinivalue_line("markers",
    #         "env(name): mark test to run only on named environment")
    # elif config.getoption('--user'):
    #     # import env
    #     # env.user_name = config.getoption('--user')
    #     user_name = config.getoption('--user')

def pytest_runtest_setup(item):
    envnames = [mark.args[0] for mark in item.iter_markers(name="env")]
    if envnames:
        if item.config.getoption("-E") not in envnames:
            pytest.skip(f"test requires env in {envnames!r}")

'''
def pytest_runtest_setup(item):
    supported_platforms = ALL.intersection(mark.name for mark in item.iter_markers())
    print(f"supported platforms={supported_platforms}")
    plat = sys.platform
    if supported_platforms and plat not in supported_platforms:
        pytest.skip("cannot run on platform {}".format(plat))

    for marker in item.iter_markers(name="env"):
        print(f"****************{marker}")
        sys.stdout.flush()

    # import pdb;pdb.set_trace()
    if not isinstance(item, pytest.Function):
        return
    # if hasattr(item.obj, 'env'):
    if hasattr(item.obj, 'pytestmark'):
        if 'env' in item.obj.pytestmark[0].name:
            envmarker = getattr(item.obj, 'env')
            envname = envmarker.args[0]
            if envname != item.config.option.env:
                pytest.skip("test requires env %r" % envname)
'''


'''
def pytest_addoption(parser):
        parser.addoption("-E", dest="env", action="store", metavar="NAME",
            help="only run tests matching the environment NAME.")

def pytest_configure(config):
    # register an additional marker
    config.addinivalue_line("markers",
        "env(name): mark test to run only on named environment")

def pytest_runtest_setup(item):
    if not isinstance(item, pytest.Function):
        return
    if hasattr(item.obj, 'env'):
        envmarker = getattr(item.obj, 'env')
        envname = envmarker.args[0]
        if envname != item.config.option.env:
            pytest.skip("test requires env %r" % envname)
'''