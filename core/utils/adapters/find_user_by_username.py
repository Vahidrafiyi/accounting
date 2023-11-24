from django.db.models   import Q

from ...models          import User

def find_user_by_username(username):
    user = User.objects.filter(
        Q(username = username) |
        Q(email     = username) |
        Q(phone     = username)
    )
    if user.exists():
        return user.first()