from django.urls import path

from djangoProject_EPMS.common.views import (
    HomeView, about
)

urlpatterns = (
    # Define the URL patterns for the common app
    path('', HomeView.as_view(), name='home'),
    path('about/', about, name='about')
)

