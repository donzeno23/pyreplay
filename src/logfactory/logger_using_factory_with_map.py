class LoggerFactory:
    
    instances = {}
    
    @staticmethod
    def register(logger_medium, instance):
        if logger_medium is not None and instance is not None:
            LoggerFactory.instances[logger_medium] = instance
    
    @staticmethod
    def get_instance(logger_medium):
        return LoggerFactory.instances.get(logger_medium, None)

