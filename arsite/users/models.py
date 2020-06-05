"""User app models."""
# django
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """User profiles model."""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )  # delete profile when user is deleted. Do not delete user if profile is deleted.
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"
