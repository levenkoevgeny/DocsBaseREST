from rest_framework import serializers
from .models import CustomUser, Subdivision, CategoryItem, DocData


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password',
                  'is_superuser',
                  'is_staff',
                  'first_name',
                  'last_name',
                  'is_active',
                  'subdivision',
                  'date_joined',
                  'last_login'
                  ]

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class SubdivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subdivision
        fields = ['subdivision_name', 'date_time_created', 'get_users_count']


class CategoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryItem
        fields = '__all__'
        depth = 1


class DocDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocData
        fields = '__all__'
        depth = 1
