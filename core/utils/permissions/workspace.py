from rest_framework.permissions import BasePermission


class WorkSpacePermission(BasePermission):
    message = {
        'detail' : 'You have not access to do this acction.'
    }

    def has_permission(self, request, view):
        user = request.user

        permission_per_action = {
            'create'        : user.role.create_workspace,
            'list'          : user.role.list_workspace,
            'retrieve'      : user.role.retrieve_workspace,
            'update'        : user.role.update_workspace,
            'partial_update': user.role.update_workspace,
            'destroy'       : user.role.destroy_workspace,
        }
        
        return permission_per_action[view.action]
