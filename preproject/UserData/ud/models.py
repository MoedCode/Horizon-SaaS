from django.db import models

# Create your models here.
from django.db import models

class UserData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    image = models.BinaryField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} <{self.email}>"