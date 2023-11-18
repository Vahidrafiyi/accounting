from rest_framework.serializers                     import ModelSerializer, PrimaryKeyRelatedField

from ..serializers.custom_tools.is_valid_serializer import IsValidSerializer

from ..serializers.user                             import OwnerSerializer

from ..modelsf.accountside_category                 import AccountSideCategory
from ..models                                       import User


class AccountSideCategorySerializer(IsValidSerializer, ModelSerializer):
    owner = PrimaryKeyRelatedField(
        queryset = User.objects.filter(is_deleted = False), 
        required = True
    )

    class Meta:
        model   = AccountSideCategory
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