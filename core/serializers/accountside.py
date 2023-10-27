from rest_framework.serializers     import ModelSerializer

from core.models.accountside        import AccountSide
from core.serializers.user          import OwnerSerializer


class AccountSideSerializer(ModelSerializer):
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