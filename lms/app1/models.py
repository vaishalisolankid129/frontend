from django.db import models

# Create your models here.
class MyModel(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.Name0


 