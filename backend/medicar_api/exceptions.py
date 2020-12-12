from rest_framework.exceptions import APIException


class InvalidHours(APIException):
    """
    Exception raised when the client tries to set an appointment in a past hour.
    """
    status_code = 400
    default_detail = 'Não é possivel marcar uma consulta para um horário no passado.'
    default_code = 'Bad Request'


class InvalidDay(APIException):
    """
        Exception raised when the client tries to set an appointment in a past day.
    """
    status_code = 400
    default_detail = 'Não é possivel marcar uma consulta para um dia no passado.'
    default_code = 'Bad Request'


class HourUnavailable(APIException):
    """
        Exception raised when the client tries to set an appointment in an hour that
        has already been taken.
    """
    status_code = 400
    default_detail = 'Este horário não está disponivel. Por favor, escolha outro'
    default_code = 'Bad Request'
