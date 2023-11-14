from rest_framework.permissions import BasePermission


class AccountSidePermission(BasePermission):
    message = {
        'detail' : 'You have not access to do this acction.'
    }

    def has_permission(self, request, view):
        user = request.user

        permission_per_action = {
            'create'        : user.role.create_accountside,
            'list'          : user.role.list_accountside,
            'retrieve'      : user.role.retrieve_accountside,
            'update'        : user.role.update_accountside,
            'partial_update': user.role.update_accountside,
            'destroy'       : user.role.destroy_accountside,
        }

        return permission_per_action[view.action]
