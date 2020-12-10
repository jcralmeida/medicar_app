from rest_framework.decorators import api_view

from medicar_api.models import Specialty
from medicar_api.serializers import SpecialtySerializer
from medicar_api.utils import prepare_response


@api_view(['GET'])
def get_specialty(request):
    """
    Get the specialty that has been already registered.

    :param request: the request received from the user.
    :return: A response in a json format.
    """

    specialty_name_filter = request.query_params.get("name")

    if(specialty_name_filter):
        retrieved_specialty = Specialty.objects.filter(name=specialty_name_filter).all()
    else:
        retrieved_specialty = Specialty.objects.filter().all()

    serialized_specialty = SpecialtySerializer(retrieved_specialty, many=True)

    json_response = prepare_response(serialized_specialty)
    return json_response

