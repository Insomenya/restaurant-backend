from .models import Order
from rest_framework import serializers

class OrderCreationSerializer(serializers.ModelSerializer):

    status = serializers.HiddenField(default='ADDED')

    class Meta:
        model = Order
        fields = ['status']