from django.contrib import admin

from djangoProject_EPMS.accounts.models import SensorsUserModel


@admin.register(SensorsUserModel)
class SensorUserModelAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_staff', 'is_superuser', 'date_joined')
    fields = ('email', 'is_active', 'is_staff', 'is_superuser', 'date_joined')
    list_filter = ('email', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', )


