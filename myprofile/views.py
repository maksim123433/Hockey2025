
from django.views.generic import TemplateView, ListView
from authorization.models import ProUser

class MyProfileView(ListView):
    template_name = 'myprofile/myprofile.html'
    model = ProUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
