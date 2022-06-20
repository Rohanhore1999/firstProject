from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from forecast.views import ForecastChartView

# def home(request):
#     return HttpResponse('Home page')

def room(request):
    return HttpResponse('Room')    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ForecastChartView.as_view(), name='home'),
    path('room/', room),
]
