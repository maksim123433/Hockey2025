from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.urls import reverse_lazy

from authorization.models import ProUser
from .models import Clubs
from .forms import ClubsForm


class ClubListView(ListView):
    model = Clubs
    template_name = "clubs/clubs.html"
    context_object_name = "clubs"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clubs = Clubs.objects.select_related('Owner', 'Head_coach').filter(Conference__in=["e", "w"])
        eastern_clubs = [club for club in clubs if club.Conference == "e"]
        western_clubs = [club for club in clubs if club.Conference == "w"]
        context["Eastern_clubs"] = eastern_clubs
        context["Western_clubs"] = western_clubs
        users = ProUser.objects.all()
        context["users"] = users

        return context


class CreateFormView(CreateView):
    model = Clubs
    template_name = "clubs/Create_clubs.html"
    form_class = ClubsForm
    success_url = reverse_lazy("clubs")

class UpdateClubView(UpdateView):
    model = Clubs
    template_name = "clubs/Create_clubs.html"
    form_class = ClubsForm
    success_url = reverse_lazy("clubs")
    pk_url_kwarg = 'pk'

class ClubInfoView(DetailView):
    model = Clubs
    template_name = "clubs/club_info.html"
    context_object_name = 'club'

    def get_object(self, queryset=None):#принимает из параметризоаного
        return self.model.objects.select_related('Owner', 'Head_coach').get(Name=self.kwargs['club_name'])


