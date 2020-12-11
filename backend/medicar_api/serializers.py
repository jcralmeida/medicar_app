from rest_framework import serializers

from medicar_api import models


class SpecialtySerializer(serializers.ModelSerializer):
    """
    Responsible to serializer an object to Json or vice-versa.
    """
    class Meta:
        model = models.Specialty
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    """
    Responsible to serializer an object to Json or vice-versa.
    """

    specialty = SpecialtySerializer(many=False, read_only=True)

    class Meta:
        model = models.Doctor
        fields = ['id', 'name', 'crm', 'email', 'phone', 'specialty']


class ScheduleSerializer(serializers.ModelSerializer):
    """
    Responsible to serializer an object to Json or vice-versa.
    """
    doctor = DoctorSerializer(many=False, read_only=True)
    time = serializers.ListField(child=serializers.TimeField(format='%H:%M'))

    class Meta:
        model = models.Schedule
        fields = ['id', 'doctor', 'date', 'time']

