from rest_framework.serializers         import ModelSerializer

from ..serializers.is_valid_serializer  import IsValidSerializer
from ..serializers.user                 import OwnerSerializer

from ..modelsf.accountside              import AccountSide


class AccountSideSerializer(IsValidSerializer, ModelSerializer):
    owner = OwnerSerializer()

    class Meta:
        model   = AccountSide
        fields  = [
            'id', 
            'created_at',
            'owner',
            'category',
            'name',
            'phone',
            'is_natural_person',
            'description',
            'received_money',
            'paid_money',
            'balance',
        ]