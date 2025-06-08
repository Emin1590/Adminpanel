from django.db import models
from django.contrib.auth.models import User

class Statistics(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_todos = models.IntegerField(default=0)
    completed_todos = models.IntegerField(default=0)
    total_tasks = models.IntegerField(default=0)
    last_login = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} üçün statistika"
