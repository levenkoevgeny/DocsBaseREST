from rest_framework import serializers
from .models import CustomUser, Subdivision, CategoryItem, DocData


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        depth = 1


class SubdivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subdivision
        fields = '__all__'


class CategoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryItem
        fields = '__all__'


class DocDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocData
        fields = '__all__'
