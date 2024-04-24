from .models import Meal
from rest_framework import serializers

class MealsListSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=40)
    price = serializers.DecimalField(max_digits=7, decimal_places=2)
    times_ordered = serializers.IntegerField(default=0)
    description = serializers.CharField(max_length=1000)
    category_name = serializers.CharField(source='category.name')
    added_at = serializers.DateTimeField()
    img = serializers.ReadOnlyField(source='image_medium.url')

    class Meta:
        model = Meal
        fields = ['id', 'name', 'price', 'times_ordered', 'description', 'category_name', 'added_at', 'img']


class SpecificMealSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=40)
    price = serializers.DecimalField(max_digits=7, decimal_places=2)
    description = serializers.CharField(max_length=1000)
    category_name = serializers.CharField(source='category.name')
    added_at = serializers.DateTimeField()
    img = serializers.ReadOnlyField(source='image_large.url')

    class Meta:
        model = Meal
        fields = ['id', 'name', 'price', 'description', 'category_name', 'added_at', 'img']