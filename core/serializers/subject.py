from rest_framework.serializers                     import ModelSerializer, PrimaryKeyRelatedField

from ..serializers.custom_tools.is_valid_serializer import IsValidSerializer
from ..serializers.user                             import OwnerSerializer
from ..serializers.subject_category                 import SubjectCategorySerializer

from ..modelsf.subject                              import Subject
from ..modelsf.subject_category                     import SubjectCategory
from ..models                                       import User


class SubjectSerializer(IsValidSerializer, ModelSerializer):
    owner = PrimaryKeyRelatedField(
        queryset = User.objects.filter(is_deleted = False),
        required = True
    )
    category = PrimaryKeyRelatedField(
        queryset = SubjectCategory.objects.filter(is_deleted = False),
        required = True
    )


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

    def to_representation(self, instance):
        self.fields['owner'] = OwnerSerializer()
        self.fields['category'] = SubjectCategorySerializer()
        return super().to_representation(instance)