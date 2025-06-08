# base_admin.py
from django.contrib import admin

class BaseAdmin(admin.ModelAdmin):
    search_fields = ['created_at']
    list_filter = ['created_at']
    list_display = ['id', 'created_at']



class BaseAdmin(admin.ModelAdmin):
    # Siyahıda görünəcək əsas sütunlar
    list_display = ['id', 'created_at', 'updated_at']

    # Axtarış üçün sahələr
    search_fields = ['created_at', 'updated_at']

    # Filtr üçün sahələr
    list_filter = ['created_at', 'updated_at']

    # Sıralama
    ordering = ['-created_at']
