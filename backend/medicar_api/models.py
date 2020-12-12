from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

class Specialty(models.Model):
    """
    The Specialty represents the model for Specialty table.
    """

    nome = models.CharField(max_length=60)

    class Meta:
        db_table = 'specialty'


class Doctor(models.Model):
    """
    The Doctor class represents the model for the Doctor table.
    """
    nome = models.CharField(max_length=60)
    crm = models.IntegerField()
    email = models.CharField(max_length=120)
    telefone = models.CharField(max_length=60, null=True)
    especialidade = models.ForeignKey(Specialty, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Schedule(models.Model):
    """
    The Schedule class represents the model for the Schedule table.
    """

    id = models.AutoField(primary_key=True, unique=True)
    medico = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    dia = models.DateField(auto_now=False, auto_now_add=False)
    horario = ArrayField(models.TimeField(auto_now=False))

    class Meta:
        db_table = 'schedule'


class Appointments(models.Model):
    """
    The Appointments class represents the model for the Appointments table.
    """

    medico = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    dia = models.DateField(auto_now=False, auto_now_add=False)
    hora = models.TimeField(auto_now=False, auto_now_add=False)
    data_agendamento =models.DateField()

    class Meta:
        db_table = 'Appointments'
