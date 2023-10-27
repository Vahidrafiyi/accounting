from rest_framework.serializers import ModelSerializer

from core.models.subject        import Subject
from core.serializers.user      import OwnerSerializer


class SubjectSerializer(ModelSerializer):
    owner = OwnerSerializer()
    
    class Meta:
        model   = Subject
        fields  = [
            'id', 
            'created_at',
            'owner',
            'category',
            'title',
            'description',
        ]