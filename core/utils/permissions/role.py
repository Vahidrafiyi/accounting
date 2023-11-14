from rest_framework.permissions import BasePermission


class RolePermission(BasePermission):
    message = {
        'detail' : 'You have not access to do this acction.'
    }

    def has_permission(self, request, view):
        user = request.user

        permission_per_action = {
            'create'        : user.role.create_role,
            'list'          : user.role.list_role,
            'retrieve'      : user.role.retrieve_role,
            'update'        : user.role.update_role,
            'partial_update': user.role.update_role,
            'destroy'       : user.role.destroy_role,
        }

        return permission_per_action[view.action]
