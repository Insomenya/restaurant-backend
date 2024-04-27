from .models import Meal, Category
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from . import serializers
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class MealsListView(generics.GenericAPIView):

    serializer_class = serializers.MealsListSerializer
    queryset = Meal.objects.all()

    @swagger_auto_schema(operation_summary='Получение полного меню')
    def get(self, request):

        meals = Meal.objects.all()

        serializer = self.serializer_class(instance=meals, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class PopularMealsView(generics.GenericAPIView):
    serializer_class = serializers.MealsListSerializer

    @swagger_auto_schema(operation_summary='Получение списка популярных блюд, количество - POPULAR_LIMIT в настройках')
    def get(self, request):
        limit = settings.POPULAR_LIMIT

        popular = Meal.objects.all().order_by('-times_ordered')[:limit]
        
        serializer = self.serializer_class(instance=popular, many=True)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
class SpecificMealView(generics.GenericAPIView):

    serializer_class = serializers.SpecificMealSerializer

    @swagger_auto_schema(operation_summary='Получение информации о конкретном блюде')
    def get(self, request, meal_id):

        meal = get_object_or_404(Meal, pk=meal_id)

        serializer = self.serializer_class(instance=meal)

        return Response(data=serializer.data, status=status.HTTP_200_OK)