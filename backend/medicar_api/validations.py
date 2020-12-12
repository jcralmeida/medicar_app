from datetime import date

from medicar_api.exceptions import InvalidHours, InvalidDay, HourUnavailable, NonExistenceAppointment
from medicar_api.models import Schedule, Appointments


def validate_hour(request_dict: dict, now: str):
    """
    Validate if the client is not trying to set an appointment to a past hour.

    :param request_dict: the request transformed into a dictionary
    :type request_dict: dict
    :param now: the hour that the client is trying to set the appointment
    :type now: str
    """
    if request_dict.get("horario") < now:
        raise InvalidHours


def validate_day(retrieved_schedule: Schedule, date_now: date):
    """
    Validate if the client is not trying to set an appointment to a past day.

    :param retrieved_schedule: a Schedule object
    :type retrieved_schedule: Schedule
    :param date_now: the hour that the client is trying to set the appointment
    :type date_now: date
    """
    if retrieved_schedule.dia < date_now:
        raise InvalidDay


def validate_appointment_available(retrieved_appointment: Appointments):
    """
    Validate if the client is not trying to set an appointment on a taken hour.

    :param retrieved_appointment: a Appointment object
    :type retrieved_appointment: Appointments
    """
    if retrieved_appointment is not None:
        raise HourUnavailable


def validate_non_existence_appointment(retrieved_appointment: Appointments):
    """
    Validate if the client is not trying delete an appointment that hadn't been created yet.

    :param retrieved_appointment: a Appointment object
    :type retrieved_appointment: Appointments
    """
    if retrieved_appointment is None:
        raise NonExistenceAppointment
