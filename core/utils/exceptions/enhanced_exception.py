from rest_framework.exceptions  import APIException
from rest_framework             import status

class EnhancedException(APIException):
    status_code = status.HTTP_200_OK
    def __init__(self, detail=None, code=None, message=None):
        if detail is None:
            detail = self.default_detail
        if code is None:
            code = self.default_code
        self.detail     = self._get_error_details(detail, message)


    def _get_error_details(self, detail, message):
        if isinstance(detail, list):
            detail = ', '.join(detail)
        return {
            'detail': detail,
            'is_success': False
        }