from django.db.models   import Q

from ...models          import User

def find_user(value):
    user = User.objects.filter(
        Q(username  = value) |
        Q(email     = value) |
        Q(phone     = value)
    )
    if user.exists():
        return user.first()