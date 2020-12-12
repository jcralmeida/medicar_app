from rest_framework.exceptions import APIException


class InvalidHours(APIException):
    """
    Exception raised when the client tries to set an appointment in a past hour.
    """
    status_code = 400
    default_detail = 'Não é possivel marcar uma consulta para um horário no passado.'
    default_code = 'Bad Request'
