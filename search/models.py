from django.db import models

# Create your models here.
class Quotes(models.Model):
    phrase = models.TextField(max_length=5000)
    author = models.CharField(max_length=200)
    source = models.CharField(max_length=500)
    topics = models.CharField(max_length=500)

    def __str__(self):
        return str(self.id)

