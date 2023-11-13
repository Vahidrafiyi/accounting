from ...modelsf.subject_category        import SubjectCategory
from ...serializers.subject_category    import SubjectCategorySerializer
from rest_framework.viewsets            import ModelViewSet


class SubjectCategoryViewset(ModelViewSet):
    def get_queryset(self):
        return SubjectCategory.objects.filter(is_deleted = False)

    serializer_class = SubjectCategorySerializer
