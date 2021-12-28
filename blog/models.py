from django.db import models
from datetime import date

class Blog(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateField(default= date.today)
    content = models.TextField()

    def __str__(self):
        return self.title
