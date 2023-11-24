from rest_framework.permissions                 import IsAuthenticated

from ...modelsf.accountside_category            import AccountSideCategory
from ...serializers.accountside_category        import AccountSideCategorySerializer
from ..enhanced_viewset.enhanced_viewset        import EnhancedCRUDModelViewSet
from ...utils.permissions.accountside_category  import AccountSideCategoryPermission

class AccountSideCategoryViewset(EnhancedCRUDModelViewSet):
    success_messages    = {
        'create'            : 'Successfully created an accountside category',
        'list'              : 'Successfully returned a list of accountside categories',
        'retrieve'          : 'Successfully retrieved an accountside category',
        'partial_update'    : 'Successfully updated an accountside category',
        'destroy'           : 'Successfully deleted an accountside category'
    }
    permission_classes  = (AccountSideCategoryPermission, IsAuthenticated)

    def get_queryset(self):
        return AccountSideCategory.objects.filter(
            is_deleted  = False, 
            owner       = self.request.user
        )

    serializer_class = AccountSideCategorySerializer

    def perform_create(self, serializer):
        return serializer.save(owner = self.request.user)
