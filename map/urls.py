from django.urls import path
from . import views


urlpatterns = [
    path('', views.render_map, name='map'),
    path('aboutus', views.render_us, name='us'),
]