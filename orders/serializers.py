from .models import Order
from rest_framework import serializers

class OrderMealSerializer(serializers.Serializer):
    meal_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

class OrderCreationSerializer(serializers.Serializer):
    status = serializers.CharField(default='ADDED')
    ordered_meals = serializers.ListField(child=OrderMealSerializer(), min_length=1)

    
class OrderSimpleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        depth = 1

class OrderStatusUpdateSerializer(serializers.ModelSerializer):

    status = serializers.CharField(default='ADDED')

    class Meta:
        model = Order
        fields = ['status']