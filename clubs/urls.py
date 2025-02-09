from django.urls import path
from clubs.views import ClubListView, CreateFormView, ClubInfoView, UpdateClubView

urlpatterns = [
    path("clubs/", ClubListView.as_view(), name="clubs"),
    path("clubs/create", CreateFormView.as_view(), name="create_club"),
    path("clubs/<int:pk>", UpdateClubView.as_view(), name="update_club"),
    path("clubs/<str:club_name>", ClubInfoView.as_view(), name="club_info"),

]
