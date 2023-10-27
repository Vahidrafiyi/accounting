from rest_framework.serializers import ModelSerializer

from core.models.note           import Note
from core.serializers.user      import OwnerSerializer


class NoteSerializer(ModelSerializer):
    owner = OwnerSerializer()

    class Meta:
        model   = Note
        fields  = [
            'id', 
            'created_at',
            'owner',
            'title',
            'description'
        ]