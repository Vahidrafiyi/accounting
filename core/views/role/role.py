from rest_framework.permissions             import IsAuthenticated

from ...modelsf.role                        import Role
from ..enhanced_viewset.enhanced_viewset    import EnhancedCRUDModelViewSet
from ...serializers.role.role               import RoleSerializer
from ...utils.permissions.role              import RolePermission


class RoleViewSet(EnhancedCRUDModelViewSet):
    success_messages = {
        'create'            : 'Successfully created a role permission',
        'list'              : 'Successfully returned a list of role permissions ',
        'retrieve'          : 'Successfully retrieved a role permission',
        'partial_update'    : 'Successfully updated a role permission',
        'destroy'           : 'Successfully deleted a role permission'
    }
    def get_queryset(self):
        return Role.objects.filter(is_deleted = False)
    
    serializer_class    = RoleSerializer
    permission_classes  = (RolePermission, IsAuthenticated)