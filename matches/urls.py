

from matches.views import MatchesView, CreateMatchesView, BuyTicketsView,UpdateMatchesView
from django.urls import path

urlpatterns = [
    path("matches/", MatchesView.as_view(), name="matches"),
    path("matches/create/", CreateMatchesView.as_view(), name="create_match"),
    path('matches/update/<int:pk>/', UpdateMatchesView.as_view(), name="update_match"),
    path('matches/buy_tickets/<int:match_id>/', BuyTicketsView.as_view(), name='buy_tickets'),
]