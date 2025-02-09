
from django.urls import path
from api.views import ClubListAPI, ProuserApiView,MathesApiView

urlpatterns = [
    path("api/clubs", ClubListAPI.as_view()),
    path("api/user", ProuserApiView.as_view()),
    path("api/match", MathesApiView.as_view()),

]
