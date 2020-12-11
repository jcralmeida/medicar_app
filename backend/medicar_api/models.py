from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

class Specialty(models.Model):
    """
    The Specialty represents the model for Specialty table.
    """

    name = models.CharField(max_length=60)

    class Meta:
        db_table = 'specialty'


class Doctor(models.Model):
    """
    The Doctor class represents the model for the Doctor table.
    """
    name = models.CharField(max_length=60)
    crm = models.IntegerField()
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=60, null=True)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    """
    The Schedule class represents the model for the Schedule table.
    """

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = ArrayField(models.TimeField(auto_now=False))

    class Meta:
        db_table = 'schedule'
