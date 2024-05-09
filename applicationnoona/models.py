from typing import Any
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=225)
    related_link = models.URLField(max_length=225)
    content = models.TextField()
    image = models.ImageField(upload_to='blog')
    data_time = models.DateTimeField()
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.titlepython