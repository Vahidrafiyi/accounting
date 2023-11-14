from rest_framework.permissions import BasePermission


class AccountSideCategoryPermission(BasePermission):
    message = {
        'detail' : 'You have not access to do this acction.'
    }

    def has_permission(self, request, view):
        user = request.user

        permission_per_action = {
            'create'        : user.role.create_accountside_category,
            'list'          : user.role.list_accountside_category,
            'retrieve'      : user.role.retrieve_accountside_category,
            'update'        : user.role.update_accountside_category,
            'partial_update': user.role.update_accountside_category,
            'destroy'       : user.role.destroy_accountside_category,
        }

        return permission_per_action[view.action]
