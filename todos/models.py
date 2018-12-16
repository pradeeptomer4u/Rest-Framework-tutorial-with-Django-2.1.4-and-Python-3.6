from django.db import models


State = (('todo', 'todo'), ('in-progress', 'in-progress'), ('done', 'done'), )

class Todo(models.Model):
    state = models.CharField(choices=State, max_length=100)
    due_date = models.DateField()
    todo_text = models.TextField()

    class Meta:
        ordering = ('due_date',)



