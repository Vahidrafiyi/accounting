from rest_framework.serializers import ModelSerializer

from core.models.account        import Account
from core.serializers.user      import OwnerSerializer


class AccountSerializer(ModelSerializer):
    owner = OwnerSerializer()

    class Meta:
        model   = Account
        fields  = [
            'id', 
            'created_at',
            'owner',
            'account_title',
            'bank_name',
            'account_number',
            'card_number',
            'shaba_number',
            'mojoudi',
            'description',
            'received_money',
            'paid_money',
            'balance',
        ]