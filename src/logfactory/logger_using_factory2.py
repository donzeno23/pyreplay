'''
logger API class level method - log to different mediums

* In memory data structure
* File on disk
* Database (local or remote)
* Remote storage service like Amazon S3 or Google Cloud Storage

In this implementation, we have separated out the individual code
into their corresponding files, but our Logger class is tigthly
coupled with the instances of the storage mediums, i.e. FileLog,
DBLog, etc...

With more additions of storage mediums, more instances will be
introduced into the Logger class
'''

class InMemoryLog:
    def log_to_memory(self, message):
        return "in-memory"
    
class FileLog:
    def log_to_file(self, message):
        return "file"
    
class DBLog:
    def log_to_db(self, message):
        return "db"
    
class RemoteServiceLog:
    def log_to_service(self, message):
        return "remote-service"

class Logger:

    def __init__(self):
        self.__mLog = InMemoryLog() # private instance variable
        self.__fLog = FileLog() # private instance variable
        self.__dbLog = DBLog() # private instance variable
        self.__sLog = RemoteServiceLog() # private instance variable

    def log(self, message, logger_medium) -> None:
        # logger_medium can be MEMORY, FILE, DB, REMOTE_SERVICE
        if logger_medium == "MEMORY":
            self.__mLog.log_to_memory(message) # private instance attribute
        elif logger_medium == "FILE":
            self.__fLog.log_to_file(message)
        elif logger_medium == "DB":
            self.__dbLog.log_to_db(message)
        elif logger_medium == "REMOTE_SERVICE":
            self.__sLog.log_to_service(message)
        else:
            print(f"Invalid log service {logger_medium} was used!")
