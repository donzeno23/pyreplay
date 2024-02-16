import importlib
# from types import ModuleType
# from pathlib import Path
import pkgutil

from replayfactory.replay_operations import ReplayOperations

class ReplayFactory(ReplayOperations):

    # instances = dict[str, ReplayOperation]
    instances = {}

    def __init__(self):
        # Assuming the package path is a directory in the filesystem
        # Replace 'package_where_storage_classes_reside' with the actual package path
        try:
            print("attempting to load classes...")
            ReplayFactory.load_classes('replayfactory')
            print("successfully loaded classes...")
        except Exception as e:
            print(f"ERROR: {e}")
            pass

    def log(self, message, logger_medium):
        print(f"logging message {message} to medium {logger_medium}")

    def connect(self): raise NotImplementedError

    def transfer(self, protocol):
        print(f"transfer protocol is {protocol}")

    @staticmethod
    def register(logger_medium, instance):
        print(f"register medium: {logger_medium} for instance: {instance}")
        if logger_medium is not None and instance is not None:
            ReplayFactory.instances[logger_medium] = instance

    @staticmethod
    def get_instance(logger_medium):
        print(f"getting instance for medium: {logger_medium}")
        return ReplayFactory.instances.get(logger_medium, None)
    
    @staticmethod
    def load_classes(package_path):
        package = package_path.replace("/", ".")
        for _, name, is_pkg in pkgutil.iter_modules([package_path]):
            if not is_pkg:
                print(f"package: {package} name: {name}")
                importlib.import_module(f"{package}.{name}")

