import csv
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Tournament, Participant
from .forms import ParticipantForm


def create_participant(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)

    if request.method == "POST":
        form = ParticipantForm(request.POST, request.FILES)
        if form.is_valid():
            participant = form.save(commit=False)
            participant.tournament = tournament
            participant.save()
            return redirect(tournament)

    else:
        form = ParticipantForm()
    return render(
        request,
        "participants/create_participant.html",
        {"tournament": tournament, "form": form},
    )


def download_participants_csv(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)
    participants = Participant.objects.filter(tournament=tournament)

    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": f"attachment;filename={tournament.name}.csv"},
    )
    writer = csv.writer(response)
    writer.writerow(
        ["Created At", "Fist Name", "Last Name", "Club", "Division", "Category"]
    )

    for participant in participants:
        writer.writerow(
            [
                participant.created_at,
                participant.first_name,
                participant.last_name,
                participant.club,
                participant.division,
                participant.category,
            ]
        )

    return response
