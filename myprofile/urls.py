from django.urls import path, include
from .views import MyProfileView

urlpatterns = [
    path("", MyProfileView.as_view(), name='myprofile'),
    path("tickets/", include('tickets.urls')),
]
