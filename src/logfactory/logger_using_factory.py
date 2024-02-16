'''
Responsibility of creating actual storage instances has been shifted
to LoggerFactory, individual storage classes just implement how they
are going to log the message to their particular medium.
Finally, the Logger class just concerns itself about getting the
appropriate storage instance through the LoggerFactory, and delegates
the actual logging to the implementation.

Now, if you want to add a new storage medium like FLASH_DRIVE, just
create a new class which implements LoggingOperation interface and
register it to the LoggerFactory with proper parameter

This is an example of how factory pattern can help you dynamically
chose an implementation
'''

from logger_factory import LoggerFactory

class Logger:

    def log(self, message, logger_medium):
        instance = LoggerFactory.get_instance(logger_medium)
        print(f"instance={instance}")
        instance.log(message)