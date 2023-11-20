from rest_framework.decorators              import action
from rest_framework.permissions             import IsAuthenticated

from ..enhanced_viewset.enhanced_viewset    import EnhancedCRUDModelViewSet
from ...models                              import User

from ...utils.adapters.get_success_response import get_success_response
from ...utils.adapters.delete_token         import delete_token
from ...utils.adapters.create_token         import create_token
from ...utils.permissions.user              import UserPermission
from ...serializers.user.user               import UserSerializer
from ...serializers.user.change_password    import ChangePasswordSerializer



class UserViewSet(EnhancedCRUDModelViewSet):
    success_messages = {
        'create'            : 'Successfully created a user',
        'list'              : 'Successfully returned a list of users ',
        'retrieve'          : 'Successfully retrieved a user',
        'partial_update'    : 'Successfully updated a user',
        'destroy'           : 'Successfully deleted a user'
    }
    def get_queryset(self):
        return User.objects.filter(is_deleted = False)
    
    serializer_class    = UserSerializer
    permission_classes  = (UserPermission, IsAuthenticated)

    @action(methods = ['post'], detail = True, url_name = 'change_password', url_path = 'change-password')
    def change_password(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data = request.data, context = self.get_serializer_context())
        serializer.is_valid(raise_exception = True)
        serializer.save()
        # Should delete previous token and create a new one after changing password
        delete_token(request.user)
        create_token(request.user)
        return get_success_response('password changed successfully')
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    