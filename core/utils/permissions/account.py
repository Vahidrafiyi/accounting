from rest_framework.permissions import BasePermission


class AccountPermission(BasePermission):
    message = {
        'detail' : 'You have not access to do this acction.'
    }

    def has_permission(self, request, view):
        user = request.user

        permission_per_action = {
            'create'        : user.role.create_account,
            'list'          : user.role.list_account,
            'retrieve'      : user.role.retrieve_account,
            'update'        : user.role.update_account,
            'partial_update': user.role.update_account,
            'destroy'       : user.role.destroy_account,
        }

        return permission_per_action[view.action]
