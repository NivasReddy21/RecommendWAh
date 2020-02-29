from django.urls import path
from django.conf.urls import url

from .views import model_form_upload

urlpatterns = [
    url('', model_form_upload, name='upload'),
]
