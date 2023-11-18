from rest_framework.serializers                     import ModelSerializer, PrimaryKeyRelatedField

from ..serializers.custom_tools.is_valid_serializer import IsValidSerializer
from ..serializers.user                             import OwnerSerializer
from ..serializers.account                          import AccountSerializer
from ..serializers.accountside                      import AccountSideSerializer
from ..serializers.subject                          import SubjectSerializer
from ..serializers.workspace                        import WorkSpaceSerializer

from ..modelsf.expense                              import Expense
from ..modelsf.account                              import Account
from ..modelsf.accountside                          import AccountSide
from ..modelsf.subject                              import Subject
from ..modelsf.workspace                            import WorkSpace
from ..models                                       import User


class ExpenseSerializer(IsValidSerializer, ModelSerializer):
    owner   = PrimaryKeyRelatedField(
        queryset = User.objects.filter(is_deleted = False),
        required = True
    )
    account = PrimaryKeyRelatedField(
        queryset = Account.objects.filter(is_deleted = False),
        required = True
    )
    accountside = PrimaryKeyRelatedField(
        queryset = AccountSide.objects.filter(is_deleted = False),
        required = True
    )
    subject = PrimaryKeyRelatedField(
        queryset = Subject.objects.filter(is_deleted = False),
        required = True
    )
    workspace = PrimaryKeyRelatedField(
        queryset = WorkSpace.objects.filter(is_deleted = False),
        required = True
    )


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

    def to_representation(self, instance):
        self.fields['owner']        = OwnerSerializer()
        self.fields['account']      = AccountSerializer()
        self.fields['accountside']  = AccountSideSerializer()
        self.fields['subject']      = SubjectSerializer()
        self.fields['workspace']    = WorkSpaceSerializer()
        return super().to_representation(instance)