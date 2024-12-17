from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.conductor_login, name='conductor_login'),
    path('ticket/',views.ticket_view,name='ticket')
    ]