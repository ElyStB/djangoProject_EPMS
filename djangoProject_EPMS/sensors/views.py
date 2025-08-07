from django.shortcuts import render

from django.views import generic as views


class SensorRegisterView(views.CreateView):
    pass


class SensorDetailView(views.DetailView):
    pass


class SensorEditView(views.UpdateView):
    pass


class SensorDeleteView(views.DeleteView):
    pass