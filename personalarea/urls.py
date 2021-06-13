from django.urls import path
from . import views
urlpatterns = [
    path('', views.show_personalarea, name="show_personalarea"),
    path('edit/', views.edit_profile, name="editprofile")
]