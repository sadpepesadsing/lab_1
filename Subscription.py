class Subscription:
    """Класс подписки"""
    def __init__(self, subscription_type: str):
        self.subscription_type = subscription_type

    def upgrade_subscription(self, new_type: str):
        """Изменить подписку"""
        assert isinstance(new_type, str) and new_type, "new type must be a non-empty string"
        self.subscription_type = new_type
        print(f"Subscription upgraded to {new_type}")