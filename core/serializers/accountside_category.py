from rest_framework.serializers                     import ModelSerializer, PrimaryKeyRelatedField

from ..serializers.custom_tools.is_valid_serializer import IsValidSerializer

from ..serializers.user.user                        import OwnerSerializer

from ..modelsf.accountside_category                 import AccountSideCategory
from ..models                                       import User


class AccountSideCategorySerializer(IsValidSerializer, ModelSerializer):

    class Meta:
        model   = AccountSideCategory
        fields  = [
            'id', 
            'created_at',
            'title',
            'description'
        ]