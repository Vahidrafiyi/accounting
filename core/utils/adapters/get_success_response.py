from rest_framework.response    import Response
from rest_framework             import status


def get_success_response(message, results = None):
    data = {
        'detail'    : message,
        'is_success': True
    }
    if results:
        data['results'] = results
    return Response(data, status = status.HTTP_200_OK)
