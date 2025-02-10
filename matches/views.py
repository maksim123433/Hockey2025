from django.views.generic import ListView, UpdateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404, redirect


from authorization.models import ProUser
from clubs.models import Clubs
from matches.models import Matches
from .forms import CreateMatch


class MatchesView(ListView):
    model = Matches
    template_name = "matches/matches.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = ProUser.objects.all()
        clubs = Clubs.objects.select_related('Owner').all()
        matches = Matches.objects.select_related('First_club', 'Second_club', 'Arbiter').all()
        context["matches"] = matches
        context["users"] = users
        context["clubs"] = clubs
        return context


class CreateMatchesView(CreateView):
    template_name = "matches/create_match.html"
    form_class = CreateMatch
    success_url = reverse_lazy("matches")


class UpdateMatchesView(UpdateView):
    template_name = "matches/create_match.html"
    model = Matches
    form_class = CreateMatch
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy("matches")


class BuyTicketsView(CreateView):
    def post(self, request, *args, **kwargs):
        match_id = kwargs['match_id']
        user = request.user
        match = get_object_or_404(Matches, id=match_id)
        if user.tickets:
            user.tickets += f',{match_id}'
        else:
            user.tickets = str(match_id)

        user.save()
        return redirect('myprofile')




