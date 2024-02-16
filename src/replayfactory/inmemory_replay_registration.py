from replayfactory.replay_factory import ReplayFactory

class InMemoryLog:

    def log(self, message):
        print(f"in-memory msg: {message}")
        return "IN-MEMORY_LOGGING"
    
    def connect(self):
        raise NotImplementedError
    
    def transfer(self, protocol):
        raise NotImplementedError    