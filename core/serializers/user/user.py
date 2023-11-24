import re

from rest_framework.serializers                         import ModelSerializer

from ...serializers.custom_tools.is_valid_serializer    import IsValidSerializer
from ..role.role                                        import MiniRoleSerializer
from ...utils.exceptions.bad_request                    import BadRequestException
from ...models                                          import User


class UserSerializer(IsValidSerializer, ModelSerializer):
    class Meta:
        model   = User
        fields  = [
            'id', 
            'created_at',
            'username',
            'phone',
            'role',
            'first_name',
            'last_name',
            'email',
            'image',
            'address',
            'date_joined'
        ]

    def to_representation(self, instance):
        self.fields['role'] = MiniRoleSerializer()
        return super().to_representation(instance)
    
    def validate_phone(self, value):
        if re.match('^(0|0098|\+98)9\d{9}$', value):
            return value
        raise BadRequestException('phone is invalid')


class OwnerSerializer(ModelSerializer):
    class Meta:
        model   = User
        fields  = [
            'id',
            'username'
        ]