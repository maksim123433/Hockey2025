from django.urls import path, include
import debug_toolbar

from main.views import MainPageView

urlpatterns = [
    path("", MainPageView.as_view(), name="main"),
    path('__debug__/', include(debug_toolbar.urls)),
]
