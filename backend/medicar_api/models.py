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