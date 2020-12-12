from datetime import datetime, date

from django.http import JsonResponse
from pytz import timezone
from rest_framework import status
from rest_framework.decorators import api_view

from medicar_api.models import Specialty, Doctor, Schedule, Appointments
from medicar_api.serializers import SpecialtySerializer, DoctorSerializer, ScheduleSerializer, AppointmentSerializer
from medicar_api.utils import prepare_response
from medicar_api.validations import validate_hour, validate_day, validate_appointment_available, \
    validate_non_existence_appointment


@api_view(['GET'])
def get_specialty(request):
    """
    Get the specialty that has been already registered.

    :param request: the request received from the user.
    :return: A response in a json format.
    """

    specialty_name_filter = request.query_params.get("nome")

    if(specialty_name_filter):
        retrieved_specialty = Specialty.objects.filter(name=specialty_name_filter).all()
    else:
        retrieved_specialty = Specialty.objects.filter().all()

    serialized_specialty = SpecialtySerializer(retrieved_specialty, many=True)

    json_response = prepare_response(serialized_specialty)
    return json_response


@api_view(['GET'])
def get_doctors(request):
    """
    Get the doctor that has been already registered.

    :param request: the request received from the user.
    :return: A response in a json format.
    """

    retrieved_specialty = Doctor.objects.filter().all()

    serialized_specialty = DoctorSerializer(retrieved_specialty, many=True)

    json_response = prepare_response(serialized_specialty)
    return json_response


@api_view(['GET'])
def get_doctors_schedule(request):
    """
    Get the schedule for a specific doctor that has been already registered.

    :param request: the request received from the user.
    :return: A response in a json format.
    """

    retrieved_schedule = Schedule.objects.filter().all()

    serialized_specialty = ScheduleSerializer(retrieved_schedule, many=True)

    json_response = prepare_response(serialized_specialty)
    return json_response


@api_view(['POST'])
def make_appointment(request):
    """
    Create an appointment for a specific doctor on a specific day and date

    :param request: the request received from the user.
    :return: A response in a json format.
    """

    request_dict = request.data

    retrieved_schedule = Schedule.objects.filter(id=request_dict.get("agenda_id")).first()

    today_date = date.today()

    fuso_horario = timezone('America/Sao_Paulo')
    now = datetime.now(fuso_horario).strftime('%H:%M')

    validate_hour(
        request_dict=request_dict,
        now=now
    )

    validate_day(
        retrieved_schedule=retrieved_schedule,
        date_now=today_date
    )

    retrieved_appointment = Appointments.objects.filter(
        hora=request_dict.get('horario'),
        dia=retrieved_schedule.dia
    ).first()

    validate_appointment_available(retrieved_appointment=retrieved_appointment)

    create = Appointments.objects.create(
        dia=retrieved_schedule.dia,
        hora=request_dict.get("horario"),
        medico=retrieved_schedule.medico,
        data_agendamento=today_date
    )

    create.save()

    appointment_serializer = AppointmentSerializer(create, many=False)

    json_response = prepare_response(appointment_serializer)

    return json_response


@api_view(['GET'])
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