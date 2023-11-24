from rest_framework.permissions             import IsAuthenticated

from ...modelsf.expense                     import Expense
from ...serializers.expense                 import ExpenseSerializer
from ..enhanced_viewset.enhanced_viewset    import EnhancedCRUDModelViewSet
from ...utils.permissions.expense           import ExpensePermission


class ExpenseViewset(EnhancedCRUDModelViewSet):
    success_messages    = {
        'create'            : 'Successfully created a expense',
        'list'              : 'Successfully returned a list of expenses',
        'retrieve'          : 'Successfully retrieved a expense',
        'partial_update'    : 'Successfully updated a expense',
        'destroy'           : 'Successfully deleted a expense'
    }
    permission_classes  = (ExpensePermission, IsAuthenticated)
    
    def get_queryset(self):
        return Expense.objects.filter(
            is_deleted  = False, 
            owner       = self.request.user
        )

    serializer_class = ExpenseSerializer

    def perform_create(self, serializer):
        return serializer.save(
            owner       = self.request.user
        )
