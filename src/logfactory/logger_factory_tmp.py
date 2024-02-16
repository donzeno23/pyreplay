'''
logger API class level method - log to different mediums

* In memory data structure
* File on disk
* Database (local or remote)
* Remote storage service like Amazon S3 or Google Cloud Storage

'''

from logging_operation import LoggingOperation
from pydoc import locate

remote_service_log_class = locate('remote_service_log_registration.RemoteServiceLog')
print(f"remote service class: {remote_service_log_class}")


def my_import(name):
    components = name.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


class LoggerFactory:
    '''
    Helps to choose the proper storage instance by examining
    the parameter - logger_medium passed to the get_instance
    method.
    '''

    instances = dict[str, LoggingOperation]

    
    try:
        load_classes()
    except Exception as e:
        print(f"caught exception: {e}")
    

    @staticmethod
    def register(logger_medium: str, instance: LoggingOperation) -> None:
        if logger_medium != None and instance != None:
            LoggerFactory.instances[logger_medium] = instance

    @staticmethod
    def get_instance(logger_medium: str) -> dict:
        if LoggerFactory.instances.__contains__(logger_medium):
            return LoggerFactory.instances[logger_medium]
        
        return {}
