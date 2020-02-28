from django.urls import path
from django.conf.urls import url

from .views import HomePageView, signup

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    url('signup/', signup, name='signup'),
]