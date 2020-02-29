from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ResultPageView(TemplateView):
    template_name = 'result.html'