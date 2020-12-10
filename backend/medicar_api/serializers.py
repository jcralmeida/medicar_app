from rest_framework import serializers

from medicar_api import models


class SpecialtySerializer(serializers.ModelSerializer):
    """
    Responsible to serializer an object to Json or vice-versa.
    """
    class Meta:
        model = models.Specialty
        fields = '__all__'
