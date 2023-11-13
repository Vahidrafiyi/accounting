from ...modelsf.subject         import Subject
from ...serializers.subject     import SubjectSerializer
from rest_framework.viewsets    import ModelViewSet


class SubjectViewset(ModelViewSet):
    def get_queryset(self):
        return Subject.objects.filter(is_deleted = False)

    serializer_class = SubjectSerializer
