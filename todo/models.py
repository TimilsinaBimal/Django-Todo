from django.db import models

# Create your models here.


class Todo(models.Model):
    complete = models.BooleanField(default=False)
    todotext = models.CharField(max_length=100)

    def __str__(self):
        return self.todotext
