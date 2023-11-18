from rest_framework.serializers                     import ModelSerializer

from ..serializers.custom_tools.is_valid_serializer import IsValidSerializer

from ..models                                       import User


# class EnhancedIsValid(ModelSerializer):
#     def is_valid(self, *, raise_exception=False):
#         return super().is_valid(raise_exception=raise_exception)


class UserSerializer(IsValidSerializer, ModelSerializer):
    class Meta:
        model   = User
        fields  = [
            'id', 
            'created_at',
            'username',
            'first_name',
            'last_name',
            'email',
            'date_joined'
        ]


class OwnerSerializer(ModelSerializer):
    class Meta:
        model   = User
        fields  = [
            'id',
            'username'
        ]