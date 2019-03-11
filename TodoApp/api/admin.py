from django.contrib import admin
from .models import TodoData


# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'complete', 'timestamp')
    search_fields = ['title', 'email', 'complete', 'timestamp']


admin.site.register(TodoData, TodoAdmin)
