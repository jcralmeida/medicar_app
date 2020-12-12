from datetime import date

from medicar_api.exceptions import InvalidHours, InvalidDay, HourUnavailable
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


