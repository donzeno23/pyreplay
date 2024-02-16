from logging_operation import LoggingOperation


class RemoteServiceLog(LoggingOperation):

    REMOTE_SERVICE = "REMOTE_SERVICE"

    @staticmethod
    def register() -> None:
        # Registration should only happen once, hence it happens when the storage classes are loaded
        RemoteServiceLog.REMOTE_SERVICE
        RemoteServiceLog()

    # @staticmethod
    # def register(RemoteServiceLog.REMOTE_SERVICE, RemoteServiceLog()):
    #     pass

    def log(self, message):
        pass