from ...modelsf.expense         import Expense
from ...serializers.expense     import ExpenseSerializer
from rest_framework.viewsets    import ModelViewSet


class ExpenseViewset(ModelViewSet):
    def get_queryset(self):
        return Expense.objects.filter(is_deleted = False)

    serializer_class = ExpenseSerializer
