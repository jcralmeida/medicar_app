from django.http import JsonResponse
from rest_framework import status


def prepare_response(serialized_object):
    """
    Prepare the response that will be shown to the user.

    :param serialized_object: a serialized object.
    :return: A response in a json format.
    """
    json_response = JsonResponse({
        'content': serialized_object.data
    },
        status=status.HTTP_200_OK)

    return json_response
