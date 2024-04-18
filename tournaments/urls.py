from django.urls import path
from . import views


urlpatterns = [
    path(
        "<uuid:tournament_id>/register/",
        views.create_participant,
        name="create_participant",
    ),
    path(
        "<uuid:tournament_id>/participants/",
        views.download_participants_csv,
        name="download_participants_csv",
    ),
]
