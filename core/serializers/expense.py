from rest_framework.serializers import ModelSerializer

from core.models.expense        import Expense
from core.serializers.user      import OwnerSerializer


class ExpenseSerializer(ModelSerializer):
    owner = OwnerSerializer()

    class Meta:
        model   = Expense
        fields  = [
            'id', 
            'created_at',
            'owner',
            'account',
            'accountside',
            'subject',
            'workspace',
            'date_time',
            'title',
            'price',
            'image',
            'is_received_money',
            'description',
        ]