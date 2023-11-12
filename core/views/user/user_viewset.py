from rest_framework.viewsets    import ModelViewSet

from ...models                  import User
from ...serializers.user        import UserSerializer

class UserViewSet(ModelViewSet):
    def get_queryset(self):
        return User.objects.filter(is_deleted = False)
    
    serializer_class = UserSerializer