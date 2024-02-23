from replayfactory.replay_factory import ReplayFactory

class FileLog:
    def log(self, message):
        print(f"FileLog: was called, using message: {message}")
        return "FILE_LOG:log"
    

    def transform(self, message):
        print("FileLog: Transforming message: {message}")
        return "FILE_LOG:transform"