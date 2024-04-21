from django.contrib import admin
from .models import Order, Meal

# Register your models here.

class OrderMealsInline(admin.TabularInline):
    model = Order.meals.through
    extra = 0
    verbose_name = 'блюдо'
    verbose_name_plural = 'блюда'

class OrderAdmin(admin.ModelAdmin):
    list_display = ['status', 'customer', 'created_at', 'updated_at']
    list_filter = ['created_at', 'status']
    inlines = [OrderMealsInline,]

admin.site.register(Order, OrderAdmin)