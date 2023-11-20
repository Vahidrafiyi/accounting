from rest_framework.serializers                         import ModelSerializer

from ...serializers.custom_tools.is_valid_serializer    import IsValidSerializer

from ...modelsf.role                                    import Role


class RoleSerializer(IsValidSerializer, ModelSerializer):
    class Meta:
        model   = Role
        fields  = [
            'id', 
            'title',
            'revoke_token',
            'create_user',
            'list_user',
            'retrieve_user',
            'update_user',
            'destroy_user',
            'create_role',
            'list_role',
            'retrieve_role',
            'update_role',
            'destroy_role',
            'create_account',
            'list_account',
            'retrieve_account',
            'update_account',
            'destroy_account',
            'create_accountside_category',
            'list_accountside_category',
            'retrieve_accountside_category',
            'update_accountside_category',
            'destroy_accountside_category',
            'create_accountside',
            'list_accountside',
            'retrieve_accountside',
            'update_accountside',
            'destroy_accountside',
            'create_expense',
            'list_expense',
            'retrieve_expense',
            'update_expense',
            'destroy_expense',
            'create_note',
            'list_note',
            'retrieve_note',
            'update_note',
            'destroy_note',
            'create_subject_category',
            'list_subject_category',
            'retrieve_subject_category',
            'update_subject_category',
            'destroy_subject_category',
            'create_subject',
            'list_subject',
            'retrieve_subject',
            'update_subject',
            'destroy_subject',
            'create_workspace',
            'list_workspace',
            'retrieve_workspace',
            'update_workspace',
            'destroy_workspace',
        ]


class MiniRoleSerializer(IsValidSerializer, ModelSerializer):
    class Meta:
        model   = Role
        fields  = [
            'id',
            'title'
        ]