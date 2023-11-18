from rest_framework.serializers                     import ModelSerializer, PrimaryKeyRelatedField

from ..serializers.custom_tools.is_valid_serializer import IsValidSerializer
from ..serializers.user                             import OwnerSerializer

from ..modelsf.note                                 import Note
from ..models                                       import User


class NoteSerializer(IsValidSerializer, ModelSerializer):
    owner = PrimaryKeyRelatedField(
        queryset = User.objects.filter(is_deleted = False),
        required = True
    )


    class Meta:
        model   = Note
        fields  = [
            'id', 
            'created_at',
            'owner',
            'title',
            'description'
        ]

    def to_representation(self, instance):
        self.fields['owner'] = OwnerSerializer()
        return super().to_representation(instance)