from django.db import models
from core.models import AbstractBaseModel
from django.urls import reverse


class Division(AbstractBaseModel):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Category(AbstractBaseModel):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Tournament(AbstractBaseModel):
    name = models.CharField(max_length=100)
    date = models.DateField()
    place = models.CharField(max_length=255)
    itinerary = models.TextField()
    divisions = models.ManyToManyField(Division)
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("create_participant", kwargs={"tournament_id": self.id})

    def get_participants_csv(self):
        return reverse("download_participants_csv", kwargs={"tournament_id": self.id})


class Participant(AbstractBaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    club = models.CharField(max_length=100, blank=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    proof_of_payment = models.FileField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
