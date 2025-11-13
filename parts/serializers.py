from rest_framework import serializers
from .models import PartCategory, Part

class PartCategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = PartCategory
        fields = ["id", "name", "parent", "children"]

    def get_children(self, obj):
        return PartCategorySerializer(obj.children.all(), many=True).data


class PartSerializer(serializers.ModelSerializer):
    category_detail = PartCategorySerializer(source="category", read_only=True)

    class Meta:
        model = Part
        fields = ["id", "name", "brand", "category", "category_detail", "description"]
