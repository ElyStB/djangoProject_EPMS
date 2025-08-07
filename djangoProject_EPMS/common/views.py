from django.views import generic as views
from django.shortcuts import render

# Create your views here.


class HomeView(views.View):
    def get(self, request):
        return render(request, 'common/home.html')


def about(request):
    return render(request, 'common/about.html')
