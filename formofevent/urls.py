from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_form_of_event, name="show_form_of_event"),
]