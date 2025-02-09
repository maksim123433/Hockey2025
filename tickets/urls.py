
from django.urls import path
from .views import MyTicketsView

urlpatterns = [
    path('', MyTicketsView.as_view(), name='my_tickets'),
]

