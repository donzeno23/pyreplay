from logging_operation import LoggingOperation
from logger_using_factory_with_class import LoggerFactory

class RemoteServiceLog(LoggingOperation):
    # Assuming LoggerFactory is a class that needs to be implemented in Python
    # and 'register' is a method that registers loggers with a specific key.
    LoggerFactory.register("REMOTE", __build_class__)

    def log(self, message):
        pass
