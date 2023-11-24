from rest_framework.permissions             import IsAuthenticated

from ...modelsf.subject_category            import SubjectCategory
from ...serializers.subject_category        import SubjectCategorySerializer
from ..enhanced_viewset.enhanced_viewset    import EnhancedCRUDModelViewSet
from ...utils.permissions.subject_category  import SubjectCategoryPermission

class SubjectCategoryViewset(EnhancedCRUDModelViewSet):
    success_messages = {
        'create'            : 'Successfully created a subject category',
        'list'              : 'Successfully returned a list of subject categories',
        'retrieve'          : 'Successfully retrieved a subject category',
        'partial_update'    : 'Successfully updated a subject category',
        'destroy'           : 'Successfully deleted a subject category'
    }
    permission_classes  = (SubjectCategoryPermission, IsAuthenticated)

    def get_queryset(self):
        return SubjectCategory.objects.filter(
            is_deleted  = False,
            owner       = self.request.user
        )

    serializer_class = SubjectCategorySerializer

    def perform_create(self, serializer):
        return serializer.save(owner = self.request.user)
