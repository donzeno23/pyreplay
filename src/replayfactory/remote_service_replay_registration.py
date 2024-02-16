from replayfactory.replay_factory import ReplayFactory

class RemoteServiceLog:

    # print("********* REMOTE *************")
    # ReplayFactory.register("REMOTE", ReplayFactory.RemoteServiceLog())
    
    @classmethod
    def register(cls):
        import pdb;pdb.set_trace()
        ReplayFactory.register("REMOTE", cls.RemoteServiceLog)

    def log(self, message):
        print(f"remote service msg: {message}")
        return "REMOTE_LOGGING"
    
    def connect(self):
        raise NotImplementedError
    
    def transfer(self, protocol):
        print(f"remote service uses {protocol} protocol")
        return protocol
