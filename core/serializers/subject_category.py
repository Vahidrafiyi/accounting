from rest_framework.serializers                     import ModelSerializer, PrimaryKeyRelatedField

from ..serializers.custom_tools.is_valid_serializer import IsValidSerializer
from ..serializers.user.user                        import OwnerSerializer

from ..models                                       import User
from ..modelsf.subject_category                     import SubjectCategory


class SubjectCategorySerializer(IsValidSerializer, ModelSerializer):
    owner = PrimaryKeyRelatedField(
        queryset = User.objects.filter(is_deleted = False),
        required = True
    )


    class Meta:
        model   = SubjectCategory
        fields  = [
            'id', 
            'created_at',
            'owner',
            'title',
            'description',
        ]

    def to_representation(self, instance):
        self.fields['owner'] = OwnerSerializer()
        return super().to_representation(instance)