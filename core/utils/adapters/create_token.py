from django.shortcuts                   import get_object_or_404

from rest_framework.authtoken.models    import Token


def create_token(user):
    try:
        return Token.objects.get_or_create(user = user)
    except:
        pass