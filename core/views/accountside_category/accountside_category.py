from ...modelsf.accountside_category        import AccountSideCategory
from ...serializers.accountside_category    import AccountSideCategorySerializer
from rest_framework.viewsets                import ModelViewSet


class AccountSideCategoryViewset(ModelViewSet):
    def get_queryset(self):
        return AccountSideCategory.objects.filter(is_deleted = False)

    serializer_class = AccountSideCategorySerializer
