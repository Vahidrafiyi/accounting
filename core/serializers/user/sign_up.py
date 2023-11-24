import re

from django.db.models                                   import Q
from django.contrib.auth.hashers                        import make_password

from rest_framework.serializers                         import (
                                                            Serializer, 
                                                            CharField, 
                                                            EmailField, 
                                                            PrimaryKeyRelatedField
                                                        )

from ...models                                          import User
from ...modelsf.role                                    import Role
from ...serializers.custom_tools.is_valid_serializer    import IsValidSerializer
from ...utils.exceptions.bad_request                    import BadRequestException
from ...utils.adapters.find_user                        import find_user

PASSWORD_REGEX_PATTERN = "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"


class SignUpSerializer(IsValidSerializer, Serializer):
    username        = CharField(required = True)
    password        = CharField(required = True)
    password_repeat = CharField(required = True)
    email           = EmailField(required = True)
    phone           = CharField(required = True)
    role            = PrimaryKeyRelatedField(
        queryset    = Role.objects.filter(is_deleted = False),
        required    = True
    )

    def validate_password(self, value):
        if not re.match(PASSWORD_REGEX_PATTERN, value):
            raise BadRequestException("password should have at least eight characters, one letter and one number")
        return value
    
    def validate_phone(self, value):
        if re.match('^9\d{9}$', value):
            return value
        raise BadRequestException('Invalid phone')
    
    def validate(self, attrs):
        username    = attrs.get('username')
        email       = attrs.get('email')
        phone       = attrs.get('phone')
        password1   = attrs.get('password')
        password2   = attrs.get('password_repeat')

        user = User.objects.filter(
            Q(username  = username) |
            Q(email     = email) |
            Q(phone     = phone)
        )
        if user.exists():
            raise BadRequestException('username, email or phone is used by another one')

        if password1 != password2:
            raise BadRequestException('passwords must be the same')
        return super().validate(attrs)
    
    def create(self, validated_data):
        user = User(
            username    = validated_data.get('username'),
            email       = validated_data.get('email'),
            phone       = validated_data.get('phone'),
            role        = validated_data.get('role')
        )
        user.password = make_password(validated_data.get('password'))
        user.save()
        return user