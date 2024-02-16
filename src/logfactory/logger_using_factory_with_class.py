import importlib
# from types import ModuleType
# from pathlib import Path
import pkgutil

# from logging_operation import LoggingOperation

class LoggerFactory:

    # instances = dict[str, LoggingOperation]
    instances = {}

    def __init__(self):
        # Assuming the package path is a directory in the filesystem
        # Replace 'package_where_storage_classes_reside' with the actual package path
        try:
            print("attempting to load classes...")
            LoggerFactory.load_classes('logfactory')
            print("successfully loaded classes...")
        except Exception as e:
            print(f"ERROR: {e}")
            pass

    @staticmethod
    def register(logger_medium, instance):
        if logger_medium is not None and instance is not None:
            LoggerFactory.instances[logger_medium] = instance

    @staticmethod
    def get_instance(logger_medium):
        print(f"getting instance for medium: {logger_medium}")
        return LoggerFactory.instances.get(logger_medium, None)
    
    @staticmethod
    def load_classes(package_path):
        package = package_path.replace("/", ".")
        for _, name, is_pkg in pkgutil.iter_modules([package_path]):
            if not is_pkg:
                importlib.import_module(f"{package}.{name}")

