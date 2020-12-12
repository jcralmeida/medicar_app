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

    especialidade = SpecialtySerializer(many=False, read_only=True)

    class Meta:
        model = models.Doctor
        fields = ['id', 'nome', 'crm', 'email', 'telefone', 'especialidade']


class ScheduleSerializer(serializers.ModelSerializer):
    """
    Responsible to serializer an object to Json or vice-versa.
    """
    medico = DoctorSerializer(many=False, read_only=True)
    horario = serializers.ListField(child=serializers.TimeField(format='%H:%M'))

    class Meta:
        model = models.Schedule
        fields = ['id', 'medico', 'dia', 'horario']


class AppointmentSerializer(serializers.ModelSerializer):
    """

    """
    medico = DoctorSerializer(many=False, read_only=True)

    class Meta:
        model = models.Appointments
        fields = ['id', 'hora', 'dia', 'data_agendamento', 'medico']

