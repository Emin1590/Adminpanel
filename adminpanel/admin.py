# admin.py
from django.contrib import admin
from .models import Note, ToDo
from .base_admin import BaseAdmin

@admin.register(Note)
class NoteAdmin(BaseAdmin):
    search_fields = BaseAdmin.search_fields + ['title', 'content']
    list_filter = BaseAdmin.list_filter + ['is_important']
    list_display = BaseAdmin.list_display + ['title', 'user']

@admin.register(ToDo)
class ToDoAdmin(BaseAdmin):
    search_fields = BaseAdmin.search_fields + ['title', 'description']
    list_filter = BaseAdmin.list_filter + ['is_completed']
    list_display = BaseAdmin.list_display + ['title', 'deadline', 'user']

from django.contrib import admin
from .models import ToDo, Note, Statistics
from .base_admin import BaseAdmin

@admin.register(ToDo)
class ToDoAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ['title', 'user', 'is_completed', 'deadline']
    search_fields = BaseAdmin.search_fields + ['title', 'description', 'user__username']
    list_filter = BaseAdmin.list_filter + ['is_completed', 'priority']

@admin.register(Note)
class NoteAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ['title', 'user', 'is_important']
    search_fields = BaseAdmin.search_fields + ['title', 'content']
    list_filter = BaseAdmin.list_filter + ['is_important']

