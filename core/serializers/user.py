from rest_framework.serializers import ModelSerializer

from core.models.user           import User


# class EnhancedIsValid(ModelSerializer):
#     def is_valid(self, *, raise_exception=False):
#         return super().is_valid(raise_exception=raise_exception)


class UserSerializer(ModelSerializer):
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