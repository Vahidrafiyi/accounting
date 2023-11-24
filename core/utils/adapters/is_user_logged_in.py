from rest_framework.authtoken.models    import Token

def is_user_logged_in(user):
    token = Token.objects.filter(user = user)
    return True if token.exists() else False