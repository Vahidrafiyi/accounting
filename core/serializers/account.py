from rest_framework.serializers                     import ModelSerializer, PrimaryKeyRelatedField

from ..serializers.custom_tools.is_valid_serializer import IsValidSerializer

from ..modelsf.account                              import Account
from ..models                                       import User
from ..serializers.user.user                        import OwnerSerializer


class AccountSerializer(IsValidSerializer, ModelSerializer):

    class Meta:
        model   = Account
        fields  = [
            'id', 
            'created_at',
            'account_title',
            'bank_name',
            'account_number',
            'card_number',
            'shaba_number',
            'description',
            'received_money',
            'paid_money',
            'balance',
        ]
