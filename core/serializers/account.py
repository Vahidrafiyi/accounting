from rest_framework.serializers                     import ModelSerializer, PrimaryKeyRelatedField

from ..serializers.custom_tools.is_valid_serializer import IsValidSerializer

from ..modelsf.account                              import Account
from ..models                                       import User
from ..serializers.user.user                        import OwnerSerializer


class AccountSerializer(IsValidSerializer, ModelSerializer):
    owner = PrimaryKeyRelatedField(
        queryset = User.objects.filter(is_deleted = False), 
        required = True
    )

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

    def to_representation(self, instance):
        self.fields['owner'] = OwnerSerializer()
        return super().to_representation(instance)
