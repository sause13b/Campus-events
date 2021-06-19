from django.urls import path
from . import views
urlpatterns = [
    path('', views.show_personalarea, name="show_personalarea"),
    path('edit/', views.edit_profile, name="editprofile"),
    path('planed/', views.planed_events, name="planed_events"),
    path('myevents/', views.my_events, name="my_events"),
    path('ended/', views.ended_events, name="ended_events")

]