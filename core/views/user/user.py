from rest_framework.viewsets                import ModelViewSet
from rest_framework.decorators              import action

from ...models                              import User
from ..enhanced_viewset.enhanced_viewset    import EnhancedCRUDModelViewSet
from ...utils.adapters.get_success_response import get_success_response
from ...utils.adapters.delete_token         import delete_token
from ...utils.adapters.create_token         import create_token
from ...serializers.user.user               import UserSerializer
from ...serializers.user.change_password    import ChangePasswordSerializer


class UserViewSet(EnhancedCRUDModelViewSet):
    def get_queryset(self):
        return User.objects.filter(is_deleted = False)
    
    serializer_class = UserSerializer

    @action(methods = ['post'], detail = True, url_name = 'change_password', url_path = 'change-password')
    def change_password(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        # Should delete previous token and create a new one after changing password
        delete_token()
        create_token()
        return get_success_response('password changes successfully')

    