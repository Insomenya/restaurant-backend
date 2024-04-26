from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'date_joined', 'is_superuser']
    list_filter = ['last_login', 'date_joined', 'is_superuser']

admin.site.unregister(Group)