from rest_framework.serializers                     import ModelSerializer, PrimaryKeyRelatedField

from ..serializers.custom_tools.is_valid_serializer import IsValidSerializer

from ..serializers.user                             import OwnerSerializer
from ..serializers.accountside_category             import AccountSideCategorySerializer

from ..modelsf.accountside                          import AccountSide
from ..modelsf.accountside_category                 import AccountSideCategory 
from ..models                                       import User


class AccountSideSerializer(IsValidSerializer, ModelSerializer):
    owner       = PrimaryKeyRelatedField(
        queryset    = User.objects.filter(is_deleted = False), 
        required    = True
    )
    category    = PrimaryKeyRelatedField(
        queryset    = AccountSideCategory.objects.filter(is_deleted = False),
        required    = True
    )


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

    def to_representation(self, instance):
        self.fields['owner']    = OwnerSerializer()
        self.fields['category'] = AccountSideCategorySerializer
        return super().to_representation(instance)