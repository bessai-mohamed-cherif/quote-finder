from django.db import models

# Create your models here.
class Authors(models.Model):
    author = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to="authors/images/")

    def __str__(self):
        return self.author