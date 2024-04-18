from .models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25)
    email = serializers.CharField(max_length=80)
    phone_number = PhoneNumberField(allow_null=False, allow_blank=True)
    password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password']

    def validate(self, attrs):
        username_exists = User.objects.filter(username=attrs['username']).exists()

        if username_exists:
            raise serializers.ValidationError(detail="Пользователь с таким именем уже существует")
        
        email_exists = User.objects.filter(username=attrs['email']).exists()

        if email_exists:
            raise serializers.ValidationError(detail="Пользователь с такой почтой уже существует")
        
        phonenumber_exists = User.objects.filter(username=attrs['phonenumber']).exists()

        if phonenumber_exists:
            raise serializers.ValidationError(detail="Пользователь с таким телефоном уже существует")
        
        return super().validate(attrs)