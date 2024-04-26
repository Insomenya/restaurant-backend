from django.contrib import admin
from .models import Category, Meal

# Register your models here.

@admin.register(Category)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at']

@admin.register(Meal)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'added_at', 'category', 'times_ordered']
    list_filter = ['added_at', 'category']