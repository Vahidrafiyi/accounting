from rest_framework.serializers                     import ModelSerializer, PrimaryKeyRelatedField

from ..serializers.custom_tools.is_valid_serializer import IsValidSerializer
from ..serializers.user.user                        import OwnerSerializer
from ..serializers.subject_category                 import SubjectCategorySerializer

from ..modelsf.subject                              import Subject
from ..modelsf.subject_category                     import SubjectCategory
from ..models                                       import User


class SubjectSerializer(IsValidSerializer, ModelSerializer):

    class Meta:
        model   = Subject
        fields  = [
            'id', 
            'created_at',
            'title',
            'description',
        ]