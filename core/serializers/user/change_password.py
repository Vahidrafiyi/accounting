import re

from rest_framework.serializers         import Serializer, CharField

from ..custom_tools.is_valid_serializer import IsValidSerializer
from ...utils.exceptions.bad_request    import BadRequestException

PASSWORD_REGEX_PATTERN = "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"

class ChangePasswordSerializer(IsValidSerializer, Serializer):
    new_password        = CharField(required = True)
    new_password_repeat = CharField(required = True)

    def validate_new_password(self, value):
        if not re.match(PASSWORD_REGEX_PATTERN, value):
            raise BadRequestException("password should have at least eight characters, one letter and one number")
        return value
    
    def validate(self, attrs):
        password1 = attrs.get('new_password')
        password2 = attrs.get('new_password_repeat')

        if password1 != password2:
            raise BadRequestException('passwords must be the same')
        return super().validate(attrs)
    
    def save(self):
        # A method to save the new password
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user


