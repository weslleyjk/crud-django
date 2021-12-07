from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name = "list"),
    path("<slug:slug>/", views.PostDatailView.as_view(), name="detail"),
]

