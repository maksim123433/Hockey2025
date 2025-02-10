from django.urls import path
from clubs.views import ClubListView, CreateFormView, ClubInfoView, UpdateClubView

urlpatterns = [
    path("", ClubListView.as_view(), name="clubs"),
    path("create/", CreateFormView.as_view(), name="create_club"),
    path("<int:pk>/", UpdateClubView.as_view(), name="update_club"),
    path("<str:club_name>/", ClubInfoView.as_view(), name="club_info"),

]
