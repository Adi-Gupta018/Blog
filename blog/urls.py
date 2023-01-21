from django.urls import path
from . import views


urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts", views.AllpostsView.as_view(), name="allposts"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail"),
    path("read-later",views.ReadLaterView.as_view(),name="read-later")
]
