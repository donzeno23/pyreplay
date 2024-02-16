'''
logger API class level method - log to different mediums

* In memory data structure
* File on disk
* Database (local or remote)
* Remote storage service like Amazon S3 or Google Cloud Storage

'''
from logger_interface import InMemoryLog, FileLog, DBLog, RemoteServiceLog

from logging_operation import LoggingOperation

class LoggerFactory(LoggingOperation):
    '''
    Helps to choose the proper storage instance by examining
    the parameter - logger_medium passed to the get_instance
    method.
    '''

    @staticmethod
    def get_instance(logger_medium):
        operation = None
        match logger_medium:
            case "MEMORY":
                # action 1
                operation = InMemoryLog()
            case "FILE":
                # action 2
                operation = FileLog()
            case "DB":
                # action 3
                operation = DBLog()
            case "REMOTE_SERVICE":
                # action 4
                operation = RemoteServiceLog()
            # case _:
            #     # default action
            #     print(f"incorrect operation {operation} was given")

        return operation
