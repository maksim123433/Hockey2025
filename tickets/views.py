from django.shortcuts import render
from django.views.generic import TemplateView
from matches.models import Matches
from authorization.models import ProUser
from django.views.generic import ListView
from matches.models import Matches
from authorization.models import ProUser

class MyTicketsView(ListView):
    model = Matches
    template_name = 'tickets/tickets.html'
    context_object_name = 'tickets'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        ticket_ids = [ticket_id for ticket_id in user.tickets.split(',') if ticket_id] if user.tickets else []
        context['tickets'] = Matches.objects.select_related('First_club',  'Second_club', 'Arbiter').filter(id__in=ticket_ids)
        return context
