import unittest

from replay.notification_factory import select_notification_factory


class NotificationTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True

    def test_notification_factory(self):
        provider = input("Enter the provider (FastNotify or SendBlue): ")
        notification_factory = select_notification_factory(provider)
        notification = notification_factory.create_email_notification()
        content_formatted = notification.format_content()
        ## if content_formatted:
        ##     notification.send()
        ## send_notification(notification_factory)

        self.assertTrue(content_formatted)



if __name__ == '__main__':
    unittest.main()

