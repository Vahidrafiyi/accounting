from django.shortcuts               import get_object_or_404

from rest_framework.authtoken.models import Token


def delete_token(user):
    try:
        token       = get_object_or_404(Token, user = user)
        token.delete()
    except:
        pass