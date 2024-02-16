from logging_operation import LoggingOperation


class InMemoryLog(LoggingOperation):
    def log(self, message):
        # log message to in-memory source
        return "in-memory"
    
class FileLog(LoggingOperation):
    def log(self, message):
        # log message to file
        return "file"
    
class DBLog(LoggingOperation):
    def log(self, message):
        # log message to db
        return "db"
    
class RemoteServiceLog(LoggingOperation):
    def log(self, message):
        # log message to remote service
        return "remote-service"