from django.db import models

# Create your models here.

class Specialty(models.Model):
    """
    The Specialty represents the model for Specialty table.
    """

    name = models.CharField(max_length=60)

    class Meta:
        db_table = 'specialty'

