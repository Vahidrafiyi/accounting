from rest_framework.permissions import BasePermission


class SubjectPermission(BasePermission):
    message = {
        'detail' : 'You have not access to do this acction.'
    }

    def has_permission(self, request, view):
        user = request.user

        permission_per_action = {
            'create'        : user.role.create_subject,
            'list'          : user.role.list_subject,
            'retrieve'      : user.role.retrieve_subject,
            'update'        : user.role.update_subject,
            'partial_update': user.role.update_subject,
            'destroy'       : user.role.destroy_subject,
        }

        return permission_per_action[view.action]
