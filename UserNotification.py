class UserNotification:
    def __init__(self, message: str, notification_type: str):
        assert notification_type in ["System", "Info", "Warning", "Promotion"], "Invalid notification type"
        self.message = message
        self.notification_type = notification_type

    def set_notification(self, message: str, notification_type: str):
        assert notification_type in ["Info", "Warning", "Promotion"], "Invalid notification type"
        self.message = message
        self.notification_type = notification_type

    def send_notification(self):
        print(f"Notification: {self.message} ({self.notification_type})")

    def __str__(self):
        return f"UserNotification(message={self.message}, notification_type={self.notification_type})"