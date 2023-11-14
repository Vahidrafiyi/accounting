from rest_framework.permissions import BasePermission


class NotePermission(BasePermission):
    message = {
        'detail' : 'You have not access to do this acction.'
    }

    def has_permission(self, request, view):
        user = request.user

        permission_per_action = {
            'create'        : user.role.create_note,
            'list'          : user.role.list_note,
            'retrieve'      : user.role.retrieve_note,
            'update'        : user.role.update_note,
            'partial_update': user.role.update_note,
            'destroy'       : user.role.destroy_note,
        }

        return permission_per_action[view.action]
