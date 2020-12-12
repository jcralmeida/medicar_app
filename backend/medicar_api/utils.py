from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response


def prepare_response(serialized_object):
    """
    Prepare the response that will be shown to the user.

    :param serialized_object: a serialized object.
    :return: A response in a json format.
    """
    json_response = JsonResponse(
        serialized_object.data,
        status=status.HTTP_200_OK)

    return json_response


def prepare_list_response(serialized_object, status):
    """
    Prepare the response as a list that will be shown to the user.

    :param serialized_object: a serialized object.
    :return: A response as list.
    """
    return Response(
        list(serialized_object.data),
        status=status)


def prepare_doctor_query_parameters(request):
    params = request.query_params
    query_params_dict = dict()
    for key in params.dict().keys():
        if key == "search":
            query_params_dict["nome"] = params.dict().get('search')
        elif key == 'especialidade':
            query_params_dict['especialidade'] = params.dict().get('especialidade')
    return query_params_dict