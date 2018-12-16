from django.contrib import admin
from todos.models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ("state", "due_date", "todo_text")
    list_filter = ("state", "due_date")


admin.site.register(Todo, TodoAdmin)
