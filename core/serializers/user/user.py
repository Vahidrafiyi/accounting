from rest_framework.serializers                         import ModelSerializer

from ...serializers.custom_tools.is_valid_serializer    import IsValidSerializer
from ..role.role                                        import MiniRoleSerializer

from ...models                                          import User


class UserSerializer(IsValidSerializer, ModelSerializer):
    class Meta:
        model   = User
        fields  = [
            'id', 
            'created_at',
            'username',
            'role',
            'first_name',
            'last_name',
            'email',
            'date_joined'
        ]

    def to_representation(self, instance):
        self.fields['role'] = MiniRoleSerializer()
        return super().to_representation(instance)


class OwnerSerializer(ModelSerializer):
    class Meta:
        model   = User
        fields  = [
            'id',
            'username'
        ]