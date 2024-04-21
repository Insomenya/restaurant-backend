from .models import Order
from rest_framework import serializers

class OrderCreationSerializer(serializers.ModelSerializer):

    status = serializers.HiddenField(default='ADDED')

    class Meta:
        model = Order
        fields = ['status', 'id']


class OrderDetailSerializer(serializers.ModelSerializer):

    status = serializers.CharField(default='ADDED')
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = Order
        fields = ['id', 'status', 'created_at', 'updated_at']

class OrderStatusUpdateSerializer(serializers.ModelSerializer):

    status = serializers.CharField(default='ADDED')

    class Meta:
        model = Order
        fields = ['status']