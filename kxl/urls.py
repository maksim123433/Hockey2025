from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("", include("authorization.urls")),
    path("", include("clubs.urls")),
    path("", include("matches.urls")),
    path("", include("forum.urls")),
    path("", include("myprofile.urls")),
    path("", include("api.urls")),

]
