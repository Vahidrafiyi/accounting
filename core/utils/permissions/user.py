from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    message = {
        'detail' : 'You have not access to do this acction.'
    }

    def has_permission(self, request, view):
        user = request.user

        permission_per_action = {
            'create'        : user.role.create_user,
            'list'          : user.role.list_user,
            'retrieve'      : user.role.retrieve_user,
            'update'        : user.role.update_user,
            'partial_update': user.role.update_user,
            'destroy'       : user.role.destroy_user,
            'change_password': True if user.is_staff else user.role.change_password
        }

        return permission_per_action[view.action]