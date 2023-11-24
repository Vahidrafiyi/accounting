from rest_framework.serializers                     import ModelSerializer, PrimaryKeyRelatedField

from ..serializers.custom_tools.is_valid_serializer import IsValidSerializer
from ..serializers.user.user                        import OwnerSerializer

from ..models                                       import User
from ..modelsf.subject_category                     import SubjectCategory


class SubjectCategorySerializer(IsValidSerializer, ModelSerializer):

    class Meta:
        model   = SubjectCategory
        fields  = [
            'id', 
            'created_at',
            'title',
            'description',
        ]