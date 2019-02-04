from django.db import models

# Create your models here.


class Cities(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=40)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
