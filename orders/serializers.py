from .models import Order, Order_meal
from menu.models import Meal
from rest_framework import serializers

class OrderCreationSerializer(serializers.ModelSerializer):
    status = serializers.HiddenField(default='ADDED')

    class Meta:
        model = Order
        fields = ['status']

    def create(self, validated_data) -> Order:
        new_order = Order.objects.create(
            status=validated_data['status']
        )

        new_order.save()

        return new_order

class OrderMealConnectionSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(default=1)

    class Meta:
        model = Order_meal
        fields = ['order_id', 'meal_id', 'quantity']

    def create(self, validated_data) -> Order_meal:

        connection = Order_meal.objects.create(
            order_id=validated_data['order_id'],
            meals=validated_data['meal_id'],
            quantity=validated_data['quantity']
        )

        connection.save()

        return connection
    
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