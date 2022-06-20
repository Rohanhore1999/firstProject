from django.shortcuts import render
from django.views.generic import TemplateView
from .models import forecast
# Create your views here.

class ForecastChartView(TemplateView):
    template_name = 'chart.html'
    model = forecast
    meta = {'allow_inheritance': False}

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    date = self.request.GET.get('date', None)
    state = self.request.GET.get('state', None)
    forecast_types = self.request.GET.get('forecast_types')
    print ("self", self.request.GET)
    date_choices = forecast.objects.all().exclude(
        date__isnill=True
    ).values_list('date', flat=True).order_by('-date').distinct()
    datasets = []
    
    
    
    return context
    
