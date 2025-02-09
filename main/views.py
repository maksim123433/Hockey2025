from django.views.generic import TemplateView
from authorization.models import ProUser
from clubs.models import Clubs
from matches.models import Matches
from forum.models import Comment


class MainPageView(TemplateView):
    template_name = "main/main_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        matches = Matches.objects.select_related('First_club', 'Second_club', 'Arbiter', ).all()
        clubs = Clubs.objects.select_related('Owner', 'Head_coach',).all()
        comments = Comment.objects.select_related('user').all()
        context["matches"] = matches
        context["clubs"] = clubs
        context["comments"] = comments

        return context
