from django.urls import path
from .views import ForumViews, AddCommentView, DeleteComment

urlpatterns = [
    path("forum/", ForumViews.as_view(), name="forum"),
    path("forum/add_comment/", AddCommentView.as_view(), name="add_comment"),
    path("forum/<int:comment_id>/delite", DeleteComment.as_view()   , name="delete_comment"),
]
