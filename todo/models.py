from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=150)
    Completed = models.BooleanField(default=False)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-added']