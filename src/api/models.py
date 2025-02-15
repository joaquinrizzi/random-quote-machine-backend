from django.db import models

# Create your models here.

class Quote (models.Model):
    content = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.content
