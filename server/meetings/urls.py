from django.urls import path
from . import views

urlpatterns = [
    path("api/getMeetings/", views.MeetingsListCreate.as_view()),
    path("api/getMeetings/<str:pk>", views.MeetingDetail.as_view())
]
