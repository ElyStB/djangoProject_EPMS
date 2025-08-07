from django.urls import path, include

from djangoProject_EPMS.sensors.views import SensorRegisterView, SensorDetailView, SensorEditView, SensorDeleteView



urlpatterns = (
    path("register/", SensorRegisterView.as_view(), name="register sensor"),
    path("<str:username>/sensor/<int:pk>/",
         include([
             path("", SensorDetailView.as_view(), name='details sensor'),
             path("edit/", SensorEditView.as_view(), name='edit sensor'),
             path("delete/", SensorDeleteView.as_view(), name='delete sensor'),
         ])),
)