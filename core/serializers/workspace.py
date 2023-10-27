from rest_framework.serializers import ModelSerializer

from core.models.workspace      import WorkSpace
from core.serializers.user      import OwnerSerializer


class WorkSpaceSerializer(ModelSerializer):
    owner = OwnerSerializer()
    
    class Meta:
        model   = WorkSpace
        fields  = [
            'id', 
            'created_at',
            'owner',
            'accountside',
            'description',
            'received_money',
            'paid_money',
            'balance',
        ]