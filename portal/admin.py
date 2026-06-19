from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('text', 'comment', 'date', 'user', 'priority')
    search_fields = ('text', 'comment')
    list_filter = ('date', 'priority', 'user')