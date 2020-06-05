"""Users app config."""

# django
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """User config."""

    name = "users"

    def ready(self):
        """Import user signals."""
        import users.signals
