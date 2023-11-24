from rest_framework.permissions             import IsAuthenticated

from ...modelsf.note                        import Note
from ...serializers.note                    import NoteSerializer
from ..enhanced_viewset.enhanced_viewset    import EnhancedCRUDModelViewSet
from ...utils.permissions.note              import NotePermission


class NoteViewset(EnhancedCRUDModelViewSet):
    success_messages    = {
        'create'            : 'Successfully created a note',
        'list'              : 'Successfully returned a list of notes',
        'retrieve'          : 'Successfully retrieved a note',
        'partial_update'    : 'Successfully updated a note',
        'destroy'           : 'Successfully deleted a note'
    }
    permission_classes  = (NotePermission, IsAuthenticated)
    
    def get_queryset(self):
        return Note.objects.filter(
            is_deleted  = False, 
            owner       = self.request.user
        )

    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        return serializer.save(
            owner       = self.request.user
        )
