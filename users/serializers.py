import json
from django.conf import settings
from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers, status, exceptions

from users.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False,write_only=True,)
    confirm_password = serializers.CharField(write_only=True, required=False)
    user_role = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        exclude = ( 'user_permissions','last_login','is_superuser','is_staff','date_joined',
                    'is_active','is_password_changed','is_email_verified','is_phone_number_verified')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # validate the country code is includede in the country code
        phone_number = validated_data.pop('phone_number')
        email = validated_data.pop('email')
        password = validated_data.pop('password') 
        confirm_password = validated_data.pop('confirm_password')
        user_role = validated_data.pop('user_role', 'store_owner')
        stores_fk = validated_data.pop('stores_fk',None)
        return user