from rest_framework import serializers
from .models import Region, CustomUser, Subdivision, CategoryItem, DocData


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password',
                  'is_superuser',
                  'is_staff',
                  'first_name',
                  'last_name',
                  'get_subdivision',
                  'get_region',
                  'is_active',
                  'subdivision',
                  'date_joined',
                  'last_login'
                  ]

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, required=True)


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class SubdivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subdivision
        fields = ['id', 'subdivision_name', 'region', 'get_region_name', 'date_time_created', 'get_users_count']


class CategoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryItem
        fields = ['id', 'category_item_name', 'parent_category', 'date_time_created', 'get_parent']


class DocDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocData
        fields = ['id', 'doc_file', 'category', 'region', 'file_name', 'description', 'doc_date', 'user', 'date_time_created', 'get_category', 'get_region']
