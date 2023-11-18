from django.utils.translation                           import gettext_lazy as _
from django.contrib.auth                                import authenticate

from rest_framework.serializers                         import (
                                                            Serializer, 
                                                            CharField
                                                        )
from ...utils.exceptions.bad_request                    import BadRequestException

from ...serializers.custom_tools.is_valid_serializer    import IsValidSerializer


class AuthTokenSerializer(IsValidSerializer, Serializer):
    username = CharField(
        label=_("Username"),
        write_only=True
    )
    password = CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise BadRequestException(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise BadRequestException(msg, code='authorization')

        attrs['user'] = user
        return attrs

