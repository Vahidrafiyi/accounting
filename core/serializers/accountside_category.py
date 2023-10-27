from rest_framework.serializers         import ModelSerializer

from core.models.accountside_category   import AccountSideCategory
from core.serializers.user              import OwnerSerializer


class AccountSideCategorySerializer(ModelSerializer):
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