from rest_framework.permissions             import IsAuthenticated

from ...modelsf.account                     import Account
from ...serializers.account                 import AccountSerializer
from ..enhanced_viewset.enhanced_viewset    import EnhancedCRUDModelViewSet
from ...utils.permissions.account           import AccountPermission

class AccountViewset(EnhancedCRUDModelViewSet):
    success_messages = {
        'create'            : 'Successfully created an account',
        'list'              : 'Successfully returned a list of accounts',
        'retrieve'          : 'Successfully retrieved an account',
        'partial_update'    : 'Successfully updated an account',
        'destroy'           : 'Successfully deleted an account'
    }
    permission_classes  = (AccountPermission, IsAuthenticated)

    def get_queryset(self):
        return Account.objects.filter(
            is_deleted  = False, 
            owner       = self.request.user
        )

    serializer_class = AccountSerializer

    def perform_create(self, serializer):
        return serializer.save(owner = self.request.user)
