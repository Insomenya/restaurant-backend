from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User
from . import serializers
from drf_yasg.utils import swagger_auto_schema
    
class UserCreateView(generics.GenericAPIView):

    serializer_class = serializers.UserCreationSerializer

    @swagger_auto_schema(operation_summary='Создать пользователя')
    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDetailsView(generics.GenericAPIView):
    serializer_class = serializers.UserDetailsSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary='Получить данные пользователя')
    def get(self, request):
        user = request.user

        serializer = self.serializer_class(instance=user)

        return Response(data=serializer.data, status=status.HTTP_200_OK)