from rest_framework.serializers                         import ModelSerializer, PrimaryKeyRelatedField

from ...models                                          import User
from ...serializers.custom_tools.is_valid_serializer    import IsValidSerializer


class RevokeTokenSerializer(IsValidSerializer, ModelSerializer):
    user = PrimaryKeyRelatedField(
        queryset = User.objects.filter(is_deleted = False), 
        required = True
    )