from django.shortcuts import render

from django.views import generic as views
from django.urls import reverse_lazy
from djangoProject_EPMS.sensors.forms import SensorCreateForm, SensorEditForm, SensorDeleteForm
from djangoProject_EPMS.sensors.models import SensorModel
from djangoProject_EPMS.sensors.mixins import CheckUserSensorPermissionMixin


class SensorRegisterView(CheckUserSensorPermissionMixin, views.CreateView):
    model = SensorModel
    form_class = SensorCreateForm
    success_url = reverse_lazy('home')
    template_name = 'sensors/sensor-register.html'

    def form_valid(self, form):  # set currently authenticated user who create the product to `manager`
        form = super().form_valid(form)
        self.object.user = self.request.user
        self.object.save()
        return form


class SensorDetailView(views.DetailView):
    model = SensorModel
    template_name = 'sensors/sensor-details.html'


class SensorEditView(CheckUserSensorPermissionMixin, views.UpdateView):
    template_engine = 'sensors/sensor-edit.html'
    model = SensorModel
    form_class = SensorEditForm
    success_url = reverse_lazy('details sensor')


class SensorDeleteView(CheckUserSensorPermissionMixin, views.DeleteView):
    template_name = 'sensors/sensor-delete.html'
    model = SensorModel
    form_class = SensorDeleteForm
    success_url = reverse_lazy('home')
