from django.contrib import admin

from djangoProject_EPMS.accounts.models import SensorsUserModel


@admin.register(SensorsUserModel)
class SensorUserModelAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'date_joined')
    fields = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'date_joined')
    list_filter = ('first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')
