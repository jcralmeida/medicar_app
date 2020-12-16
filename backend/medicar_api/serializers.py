from django.contrib.auth.models import User
from rest_framework import serializers

from medicar_api import models
from rest_framework.validators import UniqueValidator


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


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')