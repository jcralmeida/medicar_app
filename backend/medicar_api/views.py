from datetime import datetime, date

from django.db.models import Q
from django.http import JsonResponse
from pytz import timezone
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes

from medicar_api.models import Specialty, Doctor, Schedule, Appointments
from medicar_api.serializers import SpecialtySerializer, DoctorSerializer, ScheduleSerializer, AppointmentSerializer
from medicar_api.utils import prepare_response, prepare_list_response, prepare_doctor_query_parameters
from medicar_api.validations import validate_hour, validate_day, validate_appointment_available, \
    validate_non_existence_appointment

from medicar_api.serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        if user:
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_specialty(request):
    """
    Get the specialty that has been already registered.

    :param request: the request received from the user.
    :return: A response in a json format.
    """

    query_parameters_dict = dict()
    specialty_name_filter = request.query_params.get('search')

    if(specialty_name_filter):
        query_parameters_dict['nome'] = specialty_name_filter

    retrieved_specialty = Specialty.objects.filter(**query_parameters_dict).all()

    serialized_specialty = SpecialtySerializer(retrieved_specialty, many=True)

    return prepare_list_response(serialized_specialty, status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_doctors(request):
    """
    Get the doctor that has been already registered.

    :param request: the request received from the user.
    :return: A response in a json format.
    """

    query_params_dict = prepare_doctor_query_parameters(request)

    retrieved_specialty = Doctor.objects.filter(**query_params_dict).all()

    serialized_specialty = DoctorSerializer(retrieved_specialty, many=True)

    return prepare_list_response(serialized_specialty, status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_doctors_schedule(request):
    """
    Get the schedule for a specific doctor that has been already registered.

    :param request: the request received from the user.
    :return: A response in a json format.
    """
    today_date = date.today()

    retrieved_schedule = Schedule.objects.filter(
        dia__gte=today_date).filter(
        **request.query_params.dict()).all().order_by('dia')

    serialized_specialty = ScheduleSerializer(retrieved_schedule, many=True)

    return prepare_list_response(serialized_specialty, status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def make_appointment(request):
    """
    Create an appointment for a specific doctor on a specific day and date

    :param request: the request received from the user.
    :return: A response in a json format.
    """

    request_dict = request.data
    user_id = request.user.id

    retrieved_schedule = Schedule.objects.filter(id=request_dict.get("agenda_id")).first()

    today_date = date.today()

    fuso_horario = timezone('America/Sao_Paulo')
    now = datetime.now(fuso_horario).strftime('%H:%M')

    validate_hour(
        request_dict=request_dict,
        now=now,
        retrieved_schedule=retrieved_schedule,
        date_now=today_date
    )

    validate_day(
        retrieved_schedule=retrieved_schedule,
        date_now=today_date
    )

    retrieved_appointment = Appointments.objects.filter(Q(
        hora=request_dict.get('horario'),
        dia=retrieved_schedule.dia,
        agendador_por=user_id) | Q(hora=request_dict.get('horario'),
        dia=retrieved_schedule.dia,)
    ).first()

    validate_appointment_available(retrieved_appointment=retrieved_appointment)

    create = Appointments.objects.create(
        dia=retrieved_schedule.dia,
        hora=request_dict.get("horario"),
        medico=retrieved_schedule.medico,
        data_agendamento=today_date,
        agendador_por=user_id
    )

    create.save()

    appointment_serializer = AppointmentSerializer(create, many=False)

    json_response = prepare_response(appointment_serializer)

    return json_response


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_appointment(request):
    """
    Get an appointment for a specific doctor on a specific day and date

    :param request: the request received from the user.
    :return: A response in a json format.
    """

    user_id = request.user.id

    today_date = date.today()

    retrieved_schedule = Appointments.objects\
        .filter(dia__gte=today_date, agendador_por=user_id).all()\
        .order_by('dia')

    appointment_serializer = AppointmentSerializer(retrieved_schedule, many=True)

    return prepare_list_response(appointment_serializer, status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_appointment(request, consulta_id):
    """
    Delete an appointment that has been scheduled before.

    :param request: the request received from the user.
    :type request: WSGIRequest
    :param consulta_id: the appointment identifier
    :type consulta_id: int

    :return: A response in a json format.
    """

    retrieved_appointment = Appointments.objects.filter(
        id=consulta_id
    ).first()

    validate_non_existence_appointment(retrieved_appointment=retrieved_appointment)

    retrieved_appointment.delete()

    return JsonResponse(
        {},
        safe=False,
        status=status.HTTP_204_NO_CONTENT
    )
