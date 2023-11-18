from django.utils.translation                   import gettext_lazy as _
from django.shortcuts                           import get_object_or_404

from rest_framework.authtoken.models            import Token
from rest_framework                             import parsers, renderers
from rest_framework.decorators                  import action
from rest_framework.compat                      import coreapi, coreschema
from rest_framework.schemas                     import ManualSchema
from rest_framework.schemas                     import coreapi as coreapi_schema

from core.utils.adapters.get_success_response   import get_success_response


from ...utils.exceptions.bad_request            import BadRequestException
from ...utils.permissions.token                 import TokenPermission

from ...serializers.user.auth_token             import AuthTokenSerializer
from ...serializers.user.revoke_token           import RevokeTokenSerializer
from ..enhanced_viewset.enhanced_viewset        import EnhancedCRUDModelViewSet


class AuthTokenViewSet(EnhancedCRUDModelViewSet):
    throttle_classes    = ()
    permission_classes  = ()
    parser_classes      = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes    = (renderers.JSONRenderer,)
    serializer_class    = AuthTokenSerializer
    http_method_names   = ('post',)

    if coreapi_schema.is_enabled():
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="username",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Username",
                        description="Valid username for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def http_method_not_allowed(self, request, *args, **kwargs):
        raise BadRequestException('This method is not allowed')
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return get_success_response('Token created successfully', {'token': token.key})

    @action(methods = ['post'], detail = False, url_path = 'revoke-token', url_name = 'revoke_token', permission_classes = (TokenPermission, ))
    def revoke_token(self, request):
        serializer  = RevokeTokenSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user        = serializer.validated_data['user']
        token       = get_object_or_404(Token, user = user)
        token.delete()
        return get_success_response('Token revoked successfully')

