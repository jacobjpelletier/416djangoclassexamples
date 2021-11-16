from django.db import models


# Create your models here.
class TasksWithModels(models.Model):
    task = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.task
