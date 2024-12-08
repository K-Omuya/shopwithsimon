from django.db import models

# Create your models here.
class Member(models.Model):
    # Other fields...
    username = models.CharField(max_length=255, null=False, blank=False, default='default_username')
    password = models.CharField(max_length=128, null=False, blank=False, default='default_password')  # Add a default
    email = models.EmailField(max_length=255, null=False, blank=False, default='default@example.com')
    fullname = models.CharField(max_length=255, null=False, blank=False, default='John Doe')

    def __str__(self):
        return self.fullname