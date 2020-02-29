from django.urls import path
from django.conf.urls import url

from .views import ResultPageView

urlpatterns = [
    path('', ResultPageView.as_view(), name = 'result'),
]
