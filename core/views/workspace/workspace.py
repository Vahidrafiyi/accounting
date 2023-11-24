from rest_framework.permissions             import IsAuthenticated

from ...modelsf.workspace                   import WorkSpace
from ...serializers.workspace               import WorkSpaceSerializer
from ..enhanced_viewset.enhanced_viewset    import EnhancedCRUDModelViewSet
from ...utils.permissions.workspace         import WorkSpacePermission

class WorkSpaceViewset(EnhancedCRUDModelViewSet):
    success_messages = {
        'create'            : 'Successfully created a workspace',
        'list'              : 'Successfully returned a list of workspaces',
        'retrieve'          : 'Successfully retrieved a workspace',
        'partial_update'    : 'Successfully updated a workspace',
        'destroy'           : 'Successfully deleted a workspace'
    }
    permission_classes  = (WorkSpacePermission, IsAuthenticated)

    def get_queryset(self):
        return WorkSpace.objects.filter(
            is_deleted  = False, 
            owner       = self.request.user
        )

    serializer_class = WorkSpaceSerializer
    
    def perform_create(self, serializer):
        return serializer.save(owner = self.request.user)
