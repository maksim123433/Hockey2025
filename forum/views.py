

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Comment
from .forms import CommentForm

class ForumViews(ListView):
    model = Comment
    template_name = "forum/forum.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.all()
        context["form"] = CommentForm()
        return context

class AddCommentView(CreateView):
    template_name = "forum/forum.html"
    form_class = CommentForm
    success_url = reverse_lazy("forum")

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.save()
        return  super().form_valid(form)


class DeleteComment(DeleteView):
    model = Comment
    success_url = reverse_lazy("forum")

    def get_object(self):
        comment_id= self.kwargs['comment_id']
        return get_object_or_404(Comment, id=comment_id)








