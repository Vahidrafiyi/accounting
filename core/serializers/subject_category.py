from rest_framework.serializers     import ModelSerializer

from core.models.subject_category   import SubjectCategory
from core.serializers.user          import OwnerSerializer


class SubjectCategorySerializer(ModelSerializer):
    owner = OwnerSerializer()

    class Meta:
        model   = SubjectCategory
        fields  = [
            'id', 
            'created_at',
            'owner',
            'title',
            'description',
        ]