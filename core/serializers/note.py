from rest_framework.serializers                     import ModelSerializer, PrimaryKeyRelatedField

from ..serializers.custom_tools.is_valid_serializer import IsValidSerializer
from ..serializers.user.user                        import OwnerSerializer

from ..modelsf.note                                 import Note
from ..models                                       import User


class NoteSerializer(IsValidSerializer, ModelSerializer):

    class Meta:
        model   = Note
        fields  = [
            'id', 
            'created_at',
            'title',
            'description'
        ]