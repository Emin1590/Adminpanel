from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Statistics, ToDo, Task

@receiver(post_save, sender=User)
def create_user_statistics(sender, instance, created, **kwargs):
    if created:
        Statistics.objects.create(user=instance)

@receiver(post_save, sender=ToDo)
@receiver(post_save, sender=Task)
def update_user_statistics(sender, instance, **kwargs):
    stats, _ = Statistics.objects.get_or_create(user=instance.user)

    stats.total_todos = ToDo.objects.filter(user=instance.user).count()
    stats.completed_todos = ToDo.objects.filter(user=instance.user, is_completed=True).count()
    stats.total_tasks = Task.objects.filter(user=instance.user).count()
    stats.save()
