from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("questions/", views.QuestionListView.as_view(), name="question_list"),
    path("", include("django.contrib.auth.urls")),
]
