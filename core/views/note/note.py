from ...modelsf.note            import Note
from ...serializers.note        import NoteSerializer
from rest_framework.viewsets    import ModelViewSet


class NoteViewset(ModelViewSet):
    def get_queryset(self):
        return Note.objects.filter(is_deleted = False)

    serializer_class = NoteSerializer
