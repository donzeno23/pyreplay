import importlib
from types import ModuleType
from pathlib import Path
import pkgutil

class LoggerFactory:
    instances = {}
    
    @staticmethod
    def register(logger_medium, instance):
        if logger_medium is not None and instance is not None:
            LoggerFactory.instances[logger_medium] = instance
    
    @staticmethod
    def get_instance(logger_medium):
        return LoggerFactory.instances.get(logger_medium, None)
    
    @staticmethod
    def load_classes(package_path):
        package = package_path.replace("/", ".")
        for _, name, is_pkg in pkgutil.iter_modules([package_path]):
            if not is_pkg:
                importlib.import_module(f"{package}.{name}")

# Assuming the package path is a directory in the filesystem
# Replace 'package_where_storage_classes_reside' with the actual package path
try:
    LoggerFactory.load_classes('package_where_storage_classes_reside')
except Exception as e:
    pass
