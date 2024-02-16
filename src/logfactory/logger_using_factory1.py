'''
logger API class level method - log to different mediums

* In memory data structure
* File on disk
* Database (local or remote)
* Remote storage service like Amazon S3 or Google Cloud Storage
'''

class Logger:
    def log(self, message, logger_medium) -> None:
        # logger_medium can be MEMORY, FILE, DB, REMOTE_SERVICE
        if logger_medium == "MEMORY":
            self.log_in_memory(message)
        elif logger_medium == "FILE":
            self.log_on_file(message)
        elif logger_medium == "REMOTE_SERVICE":
            self.log_to_remote(message)
        else:
            print(f"Invalid log service {logger_medium} was used!")

    def log_in_memory(self, message):
        print("log in-memory was called")

    def log_on_file(self, message):
        print("log on file was called")

    def log_to_db(self, message):
        raise NotImplemented
    
    def log_to_remote(self,  message):
        print("log to remote was called")

