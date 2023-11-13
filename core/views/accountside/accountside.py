from ...modelsf.accountside     import AccountSide
from ...serializers.accountside import AccountSideSerializer
from rest_framework.viewsets    import ModelViewSet


class AccountSideViewset(ModelViewSet):
    def get_queryset(self):
        return AccountSide.objects.filter(is_deleted = False)

    serializer_class = AccountSideSerializer
