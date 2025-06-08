from django.contrib import admin
from .models import Statistics

@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ("user", "total_todos", "completed_todos", "total_tasks", "last_login", "updated_at")
    readonly_fields = ("updated_at",)
