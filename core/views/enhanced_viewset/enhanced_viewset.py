from rest_framework.viewsets                import ModelViewSet

from ...utils.exceptions.not_authenticated  import NotAuthenticatedException
from ...utils.exceptions.permission_denied  import PermissionDeniedException
from ...utils.exceptions.bad_request        import BadRequestException

from ...utils.adapters.get_success_response import get_success_response


class EnhancedCRUDModelViewSet(ModelViewSet):
    success_messages = {
        'create'            : 'Successfully created a ...',
        'list'              : 'Successfully returned a list of ... ',
        'retrieve'          : 'Successfully retrieved a ...',
        'partial_update'    : 'Successfully updated a ...',
        'destroy'           : 'Successfully deleted a ...'
    }
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data['detail']     = self.success_messages['list']
        response.data['is_success'] = True
        return response

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return get_success_response(self.success_messages['retrieve'], response.data)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return get_success_response(self.success_messages['create'], response.data)
    
    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        return get_success_response(self.success_messages['partial_update'], response.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return get_success_response(self.success_messages['destroy'])

    def perform_destroy(self, instance):
        instance.is_deleted = False
        instance.save()

    def get_object(self):
        try:
            return super().get_object()
        except Exception as e:
            raise BadRequestException(str(e)) from e
        
    def permission_denied(self, request, message=None, code=None):
        """
        If request is not permitted, determine what kind of exception to raise.
        """
        if request.authenticators and not request.successful_authenticator:
            raise NotAuthenticatedException()
        raise PermissionDeniedException(detail=message, code=code)
