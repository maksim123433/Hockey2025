from django.urls import path, include
from .views import MyProfileView

urlpatterns = [
    path("mypage/", MyProfileView.as_view(), name='myprofile'),
    path("mypage/tickets/", include('tickets.urls')),
]
