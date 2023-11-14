from rest_framework.permissions import BasePermission


class SubjectCategoryPermission(BasePermission):
    message = {
        'detail' : 'You have not access to do this acction.'
    }

    def has_permission(self, request, view):
        user = request.user

        permission_per_action = {
            'create'        : user.role.create_subject_category,
            'list'          : user.role.list_subject_category,
            'retrieve'      : user.role.retrieve_subject_category,
            'update'        : user.role.update_subject_category,
            'partial_update': user.role.update_subject_category,
            'destroy'       : user.role.destroy_subject_category,
        }

        return permission_per_action[view.action]
