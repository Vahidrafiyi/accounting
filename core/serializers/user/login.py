from django.db.models                                   import Q
from django.contrib.auth                                import authenticate

from rest_framework.serializers                         import Serializer, CharField

from ...models                                          import User
from ...serializers.custom_tools.is_valid_serializer    import IsValidSerializer
from ...utils.exceptions.bad_request                    import BadRequestException
from ...utils.adapters.find_user_by_username            import find_user_by_username

class LoginSerializer(IsValidSerializer, Serializer):
    username = CharField(required = True)
    password = CharField(required = True)

    def validate_username(self, value):
        user = find_user_by_username(value)
        if not user:
            raise BadRequestException("Invalid username")
        return value
    
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        
        # Check if the provided credentials are valid
        user = authenticate(
            username = username,
            password = password,
        )
        if user is None:
            raise BadRequestException("Invalid password")
        return attrs
