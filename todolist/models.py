from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    status = models.BooleanField(default=False, verbose_name='Status')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated')

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

