import re

from rest_framework.serializers                     import ModelSerializer, PrimaryKeyRelatedField

from ..serializers.custom_tools.is_valid_serializer import IsValidSerializer

from ..serializers.user.user                        import OwnerSerializer
from ..serializers.accountside_category             import AccountSideCategorySerializer
from ..utils.exceptions.bad_request                 import BadRequestException
from ..modelsf.accountside                          import AccountSide
from ..modelsf.accountside_category                 import AccountSideCategory 
from ..models                                       import User


class AccountSideSerializer(IsValidSerializer, ModelSerializer):

    class Meta:
        model   = AccountSide
        fields  = [
            'id', 
            'created_at',
            'name',
            'phone',
            'is_natural_person',
            'description',
            'received_money',
            'paid_money',
            'balance',
        ]

    def validate_phone(self, value):
        if re.match('^9\d{9}$', value):
            return value
        raise BadRequestException('phone is invalid')