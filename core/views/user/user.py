from rest_framework.decorators                  import action
from rest_framework.permissions                 import IsAuthenticated

from ..enhanced_viewset.enhanced_viewset        import EnhancedCRUDModelViewSet
from ...models                                  import User

from ...utils.adapters.get_success_response     import get_success_response
from ...utils.adapters.delete_token             import delete_token
from ...utils.adapters.create_token             import create_token
from ...utils.adapters.find_user_by_username    import find_user_by_username
from ...utils.adapters.is_user_logged_in        import is_user_logged_in
from ...utils.permissions.user                  import UserPermission
from ...serializers.user.user                   import UserSerializer
from ...serializers.user.change_password        import ChangePasswordSerializer
from ...serializers.user.login                  import LoginSerializer
from ...utils.exceptions.bad_request            import BadRequestException

class UserViewSet(EnhancedCRUDModelViewSet):
    success_messages    = {
        'create'            : 'Successfully created a user',
        'list'              : 'Successfully returned a list of users ',
        'retrieve'          : 'Successfully retrieved a user',
        'partial_update'    : 'Successfully updated a user',
        'destroy'           : 'Successfully deleted a user'
    }
    serializer_class    = UserSerializer
    permission_classes  = (UserPermission, IsAuthenticated)

    def get_queryset(self):
        return User.objects.filter(is_deleted = False)
    
    @action(methods = ['post'], detail = False, url_name = 'change_password', url_path = 'change-password')
    def change_password(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data = request.data, context = self.get_serializer_context())
        serializer.is_valid(raise_exception = True)
        serializer.save()
        # Should delete previous token and create a new one after changing password
        delete_token(request.user)
        create_token(request.user)
        return get_success_response('password changed successfully')
    
    @action(methods = ['get'], detail = False, url_name = 'logout', url_path = 'logout')
    def logout(self, request, *args, **kwargs):
        try:
            token = request.user.auth_token
            token.delete()
            return get_success_response("user logged out successfully.")
        except Exception as e:
            raise BadRequestException(str(e))
        
    @action(methods = ['post'], detail = False, url_name = 'login', url_path = 'login', authentication_classes = (), permission_classes = ())
    def login(self, request, *args, **kwargs):
        serializer      = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        username        = serializer.validated_data.get('username')
        user            = find_user_by_username(username)
        is_logged_in    = is_user_logged_in(user)
        if is_logged_in:
            raise BadRequestException('user logged in already')
        token, created  = create_token(user)
        return get_success_response('user logged in successfully', {"token": token.key})


    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    