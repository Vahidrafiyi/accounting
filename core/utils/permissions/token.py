from rest_framework.permissions import BasePermission


class TokenPermission(BasePermission):
    message = {
        'detail' : 'You have not access to do this acction.'
    }

    def has_permission(self, request, view):
        user       = request.user

        permission_per_action = {
            'revoke_token'               : user.role.revoke_token,
        }

        return permission_per_action[view.action]
