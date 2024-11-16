from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from catalog.models import Material, Category


class MaterialSerializer(serializers.ModelSerializer):
    """Serializer for materials."""

    category = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Category.objects.all()
    )

    class Meta:
        model = Material
        fields = '__all__'


class MaterialInTreeSerializer(serializers.ModelSerializer):
    """Serializer for material in tree."""

    class Meta:
        model = Material
        fields = ('id', 'name', 'code', 'price')


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for categories."""

    parent = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Category.objects.all(),
        required=False
    )

    class Meta:
        model = Category
        fields = '__all__'


class TreeSerializer(serializers.ModelSerializer):
    """Serializer for tree."""

    parent = SlugRelatedField(slug_field='name', read_only=True)
    materials = serializers.SerializerMethodField()
    children = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            'name',
            'code',
            'parent',
            'materials',
            'children',
            'total_price'
        ]

    def get_children(self, obj):
        return TreeSerializer(obj.children.all(), many=True).data

    def get_materials(self, obj):
        return MaterialInTreeSerializer(obj.materials.all(), many=True).data

    def get_total_price(self, obj):
        total_price = sum(material.price for material in obj.materials.all())
        total_price += sum(
            self.get_total_price(child) for child in obj.children.all())
        return total_price

    def to_representation(self, instance):
        """Delete fields from representation if not  exists"""
        representation = super().to_representation(instance)
        for field in ('children', 'materials'):
            if not representation.get(field):
                representation.pop(field)
        return representation
