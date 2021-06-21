from django.urls import path
from . import views


urlpatterns = [
    path('<str:pk>', views.show_form_of_event, name="show_form_of_event"),
    path('pa/<str:pk>', views.show_form_of_event_pa, name="back_form"),
    path('party/<str:pk>', views.party, name='party'),
    path('leaveparty/<str:pk>', views.leave_party, name='leave_party'),
    path('editparty/<str:pk>', views.edit_party, name='edit_party')
]