from django.db import models

# Create your models here.


class Professor(models.Model):
    id = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)

    def __str__(self):
        return self.firstName


class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=10)
    professors = models.ManyToManyField('Professor', blank=True)
