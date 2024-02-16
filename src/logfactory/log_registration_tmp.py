from logging_operation import LoggingOperation


class RemoteServiceLog(LoggingOperation):

    REMOTE_SERVICE = "REMOTE"

    @staticmethod
    def register() -> None:
        # Registration should only happen once, hence it happs when the storage classes are loaded
        RemoteServiceLog.REMOTE_SERVICE
        RemoteServiceLog()

    # @staticmethod
    # def register(RemoteServiceLog.REMOTE_SERVICE, RemoteServiceLog()):
    #     pass

    def log(self, message):
        pass