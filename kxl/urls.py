from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("main/", include("main.urls")),
    path("", include("authorization.urls")),
    path("clubs/", include("clubs.urls")),
    path("matches/", include("matches.urls")),
    path("forum/", include("forum.urls")),
    path("mypage/", include("myprofile.urls")),
    path("", include("api.urls")),

]
