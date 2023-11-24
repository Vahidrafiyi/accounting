from rest_framework.serializers                     import ModelSerializer, PrimaryKeyRelatedField

from ..serializers.custom_tools.is_valid_serializer import IsValidSerializer
from ..serializers.user.user                        import OwnerSerializer
from ..serializers.accountside                      import AccountSideSerializer

from ..modelsf.workspace                            import WorkSpace
from ..models                                       import User
from ..modelsf.accountside                          import AccountSide


class WorkSpaceSerializer(IsValidSerializer, ModelSerializer):
    accountside = PrimaryKeyRelatedField(
        queryset = AccountSide.objects.filter(is_deleted = False),
        required = True
    )
    
    class Meta:
        model   = WorkSpace
        fields  = [
            'id', 
            'created_at',
            'accountside',
            'description',
            'received_money',
            'paid_money',
            'balance',
        ]

    def to_representation(self, instance):
        self.fields['accountside']  = AccountSideSerializer()
        return super().to_representation(instance)