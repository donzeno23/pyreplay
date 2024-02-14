from abc import ABC, abstractmethod

# Abstract Factory Interface
class NotificationFactory(ABC):
    """ Abstract Factory Interface """

    @abstractmethod
    def create_email_notification(self):
        pass

    @abstractmethod
    def create_sms_notification(self):
        pass

    @abstractmethod
    def create_push_notification(self):
        pass


# Concrete Factories
class FastNotifyFactory(NotificationFactory):
    """ Concrete Factory for FastNotify """

    def create_email_notification(self):
        return FastNotifyEmailNotification()
    
    def create_sms_notification(self):
        return FastNotifySMSNotification()
    
    def create_push_notification(self):
        return FastNotifyPushNotification()
    

class SendBlueFactory(NotificationFactory):
    """ Concrete Factory for SendBlue """

    def create_email_notification(self):
        return SendBlueEmailNotification()
    
    def create_sms_notification(self):
        return SendBlueSMSNotification()
    
    def create_push_notification(self):
        return SendBluePushNotification()
        

# Abstract Products
class AbstractEmailNotification(ABC):
    """ Abstract Product for Email Notifications """

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def format_content(self):
        pass


class AbstractSMSNotification(ABC):
    """ Abstract Product for SMS Notifications """

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def encode_message(self):
        pass

class AbstractPushNotification(ABC):
    """ Abstract Product for Push Notifications """

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def format_payload(self):
        pass


# Concrete Products
class FastNotifyEmailNotification(AbstractEmailNotification):
    """ Concrete Product for Email Notifications via FastNotify """

    def send(self):
        print("Sending Email via FastNotify")

    def format_content(self):
        print("Formatting Email content")
        return True


class FastNotifySMSNotification(AbstractSMSNotification):
    """ Concrete Product for SMS Notifications via FastNotify """

    def send(self):
        print("Sending SMS via FastNotify")

    def encode_message(self):
        print("Encoding SMS message")


class FastNotifyPushNotification(AbstractPushNotification):
    """ Concrete Product for Push Notifications via FastNotify """

    def send(self):
        print("Sending Push Notification via FastNotify")

    def format_payload(self):
        print("Formatting Push Notification payload")


class SendBlueEmailNotification(AbstractEmailNotification):
    """ Concrete Product for Email Notifications via SendBlue """

    def send(self):
        print("Sending Email via SendBlue")

    def format_content(self):
        print("Formatting Email content")
        return True

class SendBlueSMSNotification(AbstractSMSNotification):
    """ Concrete Product for SMS Notifications via SendBlue """

    def send(self):
        print("Sending SMS via SendBlue")

    def encode_message(self):
        print("Encoding SMS message")

class SendBluePushNotification(AbstractPushNotification):
    """ Concrete Product for Push Notifications via SendBlue """

    def send(self):
        print("Sending Push Notification via SendBlue")

    def format_payload(self):
        print("Formatting Push Notification payload")


'''
Factory Mapping: 
maps provider names (e.g. FastNotify or SendBlue)
to their respective factory classes
'''
factory_mapping = {
    "FastNotify": FastNotifyFactory(),
    "SendBlue": SendBlueFactory(),
}

'''
we take the provider as input and use it to 
look up the corresponding factory object from the
factory_mapping dictionary
'''
def select_notification_factory(provider):
    """ Select and return the Notification Factory based on the provider """
    factory = factory_mapping.get(provider)
    if factory is None:
        raise ValueError("Invalid provider")
    return factory
