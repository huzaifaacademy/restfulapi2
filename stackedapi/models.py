from django.db import models

class Employees(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)


    def __str__(self):
        return self.name