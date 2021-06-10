from django.urls import path
from . import views


urlpatterns = [
    path('', views.create_event, name="create_event"),
    path('get_data', views.get_data, name='get_data'),
]