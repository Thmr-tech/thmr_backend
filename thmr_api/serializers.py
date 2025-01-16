from djoser.serializers import UserCreatePasswordRetypeSerializer
from rest_framework import serializers
from .models import CustomUser


class UserCreateSerializer(UserCreatePasswordRetypeSerializer):
    print('test')

    class Meta(UserCreatePasswordRetypeSerializer.Meta):
        model = CustomUser
        fields = [
            'email', 'full_name', 'national_id', 'telephone', 'family_funds_box_number',
            'family_funds_box_name', 'family_funds_regulations', 'signup_type', 'password'
        ]

    def validate(self, attrs):
        # Check for a specific condition in the request
        print("Password:", attrs.get("password"))
        print("Re-Password:", attrs.get("re_password"))
        print('here', self.context['request'].data.get('signup_type'))
        if self.context['request'].data.get('signup_type') == 'manager':
            if not attrs.get('family_funds_box_name'):
                raise serializers.ValidationError({
                    'family_funds_box_name': 'This field is required for the manager signup type.'
                })
            if not attrs.get('family_funds_regulations'):
                raise serializers.ValidationError({
                    'family_funds_regulations': 'This field is required for the manager signup type.'
                })

        return super().validate(attrs)
