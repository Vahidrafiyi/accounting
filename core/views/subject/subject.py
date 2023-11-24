from rest_framework.permissions             import IsAuthenticated

from ...modelsf.subject                     import Subject
from ...serializers.subject                 import SubjectSerializer
from ..enhanced_viewset.enhanced_viewset    import EnhancedCRUDModelViewSet
from ...utils.permissions.subject           import SubjectPermission


class SubjectViewset(EnhancedCRUDModelViewSet):
    success_messages    = {
        'create'            : 'Successfully created a subject',
        'list'              : 'Successfully returned a list of subjects',
        'retrieve'          : 'Successfully retrieved a subject',
        'partial_update'    : 'Successfully updated a subject',
        'destroy'           : 'Successfully deleted a subject'
    }
    permission_classes  = (SubjectPermission, IsAuthenticated)
    
    def get_queryset(self):
        return Subject.objects.filter(
            is_deleted  = False, 
            owner       = self.request.user, 
            category_id = self.kwargs.get('subject_category_pk')
        )

    serializer_class = SubjectSerializer

    def perform_create(self, serializer):
        return serializer.save(
            owner       = self.request.user, 
            category_id = self.kwargs.get('subject_category_pk')
        )
