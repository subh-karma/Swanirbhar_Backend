from django.db import models

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Course(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    instructor = models.ForeignKey(User, related_name='courses', on_delete=models.CASCADE)

    def __str__(self):
        return self.title