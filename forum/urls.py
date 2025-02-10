from django.urls import path
from .views import ForumViews, AddCommentView, DeleteComment

urlpatterns = [
    path("", ForumViews.as_view(), name="forum"),
    path("add_comment/", AddCommentView.as_view(), name="add_comment"),
    path("<int:comment_id>/delite", DeleteComment.as_view()   , name="delete_comment"),
]
