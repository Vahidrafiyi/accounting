from rest_framework.serializers         import ModelSerializer

from ..serializers.is_valid_serializer  import IsValidSerializer
from ..serializers.user                 import OwnerSerializer

from ..modelsf.accountside_category     import AccountSideCategory


class AccountSideCategorySerializer(IsValidSerializer, ModelSerializer):
    owner = OwnerSerializer()

    class Meta:
        model   = AccountSideCategory
        fields  = [
            'id', 
            'created_at',
            'owner',
            'title',
            'description'
        ]