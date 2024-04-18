from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Division, Category, Tournament, Participant

admin.site.register([Division, Category])


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ["name", "date", "tournament_url", "participants_csv"]

    def tournament_url(self, obj):
        return mark_safe(f'<a href="{obj.get_absolute_url()}" target="_blank">Link</a>')

    tournament_url.short_description = "Registration Form"

    def participants_csv(self, obj):
        return mark_safe(f'<a href="{obj.get_participants_csv()}">Download</a>')

    participants_csv.short_description = "Participants"


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ["name", "tournament_name", "proof_of_payment"]

    def name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    def tournament_name(self, obj):
        return obj.tournament.name
