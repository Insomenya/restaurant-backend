import collections.abc
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers
from .models import Order, Order_meal
from menu.models import Meal
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

class OrderListView(generics.GenericAPIView):

    serializer_class = serializers.OrderSimpleListSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary='Просмотр списка заказов для авторизованных пользователей')
    def get(self, request):
        user = request.user

        orders = Order.objects.all().filter(customer=user)

        serializer = self.serializer_class(instance=orders, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class OrderCreationView(generics.GenericAPIView):
    serializer_class = serializers.OrderCreationSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary='Создание заказа авторизованным пользователем')
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        user = request.user

        if serializer.is_valid():
            if isinstance(serializer.data['ordered_meals'], collections.abc.Sequence):
                def getMealId(meal):
                    return meal['meal_id']
                
                def getQuantity(meal):
                    return meal['quantity']

                validated_data = serializer.data
                new_order = Order.objects.create(customer=user, status=validated_data['status'])
                new_order.save()

                order_ids = [new_order.id] * len(validated_data['ordered_meals'])
                meal_ids = map(getMealId, validated_data['ordered_meals'])
                quantities = map(getQuantity, validated_data['ordered_meals'])

                connections_data = zip(
                    meal_ids,
                    quantities
                )

                for conn in connections_data:
                    existing_meal = Meal.objects.filter(id=conn[0])

                    if existing_meal.exists():
                        new_connection = Order_meal.objects.create(order=new_order, meal=existing_meal.first(), quantity=conn[1])

                        new_connection.save()

                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminSpecificOrderView(generics.GenericAPIView):
    serializer_class = serializers.OrderSimpleListSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    @swagger_auto_schema(operation_summary='Просмотр сведений о конкретном заказе администратором')
    def get(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)

        serializer = self.serializer_class(instance=order)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary='Изменение заказа администратором')
    def put(self, request, order_id):
        data = request.data

        order = get_object_or_404(Order, pk=order_id)

        serializer = self.serializer_class(data=data, instance=order)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary='Удаление заказа администратором')
    def delete(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)

        order.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class UpdateOrderStatusView(generics.GenericAPIView):

    serializer_class = serializers.OrderStatusUpdateSerializer

    permission_classes = [IsAuthenticated, IsAdminUser]
    
    @swagger_auto_schema(operation_summary='Обновление статуса заказа администратором')
    def put(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)

        data = request.data

        serializer = self.serializer_class(data=data, instance=order)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CancellOrderView(generics.GenericAPIView):

    serializer_class = serializers.OrderStatusUpdateSerializer

    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(operation_summary='Отмена заказа авторизованным пользователем')
    def put(self, request, order_id):
        user = request.user

        try:
            order = Order.objects.all().filter(customer=user).get(pk=order_id)
        except Order.DoesNotExist:
            return Response(data={"detail": "No Order matches the given query."}, status=status.HTTP_404_NOT_FOUND)

        data = {
            'status': 'CANCELLED'
        }

        serializer = self.serializer_class(data=data, instance=order)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserSpecificOrderView(generics.GenericAPIView):
    serializer_class = serializers.OrderSimpleListSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary='Просмотр конкретного заказа для авторизованного пользователя')
    def get(self, request, order_id):
        user = request.user

        orders = Order.objects.all().filter(customer=user).get(pk=order_id)

        serializer = self.serializer_class(instance=orders)

        return Response(data=serializer.data, status=status.HTTP_200_OK)