from ...modelsf.workspace       import WorkSpace
from ...serializers.workspace   import WorkSpaceSerializer
from rest_framework.viewsets    import ModelViewSet


class WorkSpaceViewset(ModelViewSet):
    def get_queryset(self):
        return WorkSpace.objects.filter(is_deleted = False)

    serializer_class = WorkSpaceSerializer
