from django.db import models

from django.db import models
from django.contrib.auth import get_user_model
from courses.models import Course

User = get_user_model()

class Progress(models.Model):
    user = models.ForeignKey(User, related_name='progress', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='progress', on_delete=models.CASCADE)
    progress = models.FloatField()

    def __str__(self):
        return f'{self.user.username} - {self.course.title} - {self.progress}%'
