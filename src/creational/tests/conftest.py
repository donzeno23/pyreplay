import sys
import pytest


import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print(sys.path)

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

def pytest_runtest_setup(item):
    envnames = [mark.args[0] for mark in item.iter_markers(name="env")]
    if envnames:
        if item.config.getoption("-E") not in envnames:
            pytest.skip(f"test requires env in {envnames!r}")
