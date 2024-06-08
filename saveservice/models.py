from django.db import models

# Create your models here.

from django.db import models

class mymodel(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()


    def __str__(self):
        return self.name


