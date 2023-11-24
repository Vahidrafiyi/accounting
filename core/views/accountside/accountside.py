from rest_framework.permissions             import IsAuthenticated

from ...modelsf.accountside                 import AccountSide
from ...serializers.accountside             import AccountSideSerializer
from ..enhanced_viewset.enhanced_viewset    import EnhancedCRUDModelViewSet
from ...utils.permissions.accountside       import AccountSidePermission

class AccountSideViewset(EnhancedCRUDModelViewSet):
    success_messages    = {
        'create'            : 'Successfully created an accountside',
        'list'              : 'Successfully returned a list of accountsides',
        'retrieve'          : 'Successfully retrieved an accountside',
        'partial_update'    : 'Successfully updated an accountside',
        'destroy'           : 'Successfully deleted an accountside'
    }
    permission_classes  = (AccountSidePermission, IsAuthenticated)
    
    def get_queryset(self):
        return AccountSide.objects.filter(
            is_deleted  = False, 
            owner       = self.request.user, 
            category_id = self.kwargs.get('accountside_category_pk')
        )

    serializer_class = AccountSideSerializer

    def perform_create(self, serializer):
        return serializer.save(
            owner       = self.request.user, 
            category_id = self.kwargs.get('accountside_category_pk')
        )
