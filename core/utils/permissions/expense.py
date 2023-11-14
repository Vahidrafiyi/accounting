from rest_framework.permissions import BasePermission


class ExpensePermission(BasePermission):
    message = {
        'detail' : 'You have not access to do this acction.'
    }

    def has_permission(self, request, view):
        user = request.user

        permission_per_action = {
            'create'        : user.role.create_expense,
            'list'          : user.role.list_expense,
            'retrieve'      : user.role.retrieve_expense,
            'update'        : user.role.update_expense,
            'partial_update': user.role.update_expense,
            'destroy'       : user.role.destroy_expense,
        }

        return permission_per_action[view.action]
