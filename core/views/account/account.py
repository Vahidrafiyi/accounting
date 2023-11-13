from ...modelsf.account         import Account
from ...serializers.account     import AccountSerializer
from rest_framework.viewsets    import ModelViewSet


class AccountViewset(ModelViewSet):
    def get_queryset(self):
        return Account.objects.filter(is_deleted = False)

    serializer_class = AccountSerializer
