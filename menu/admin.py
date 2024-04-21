from django.contrib import admin
from .models import Category, Meal

# Register your models here.

@admin.register(Category)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']

@admin.register(Meal)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'added_at', 'times_ordered']
    list_filter = ['name', 'added_at', 'category']