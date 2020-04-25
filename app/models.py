from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.CharField(max_length=255, null=True)
    twitter = models.CharField(max_length=255, null=True)
    discord = models.CharField(max_length=255, null=True)
    twitch = models.CharField(max_length=255, null=True)
    youtube = models.CharField(max_length=255, null=True)
    instagram = models.CharField(max_length=255, null=True)
    facebook = models.CharField(max_length=255, null=True)

    def is_created(self, user):
        existCount = Profile.objects.filter(pk = user.pk)
        output = None
        if existCount == 1:
            output = True
        elif existCount == 0:
            output = False
        else:
            print("Warning: Profile duplicates")

        return output

class Game(models.Model):
    name = models.CharField(max_length=255, null=True)
    def get_abname(self):
        abname = ""
        if self.name == "Overwatch":
            abname = "ow"
        elif self.name == "Tom Clancy's Rainbow Six Siege":
            abname = "r6"
        elif self.name == "League of Legend":
            abname = "lol"
        elif self.name == "Rocket League":
            abname = "rl"
        else:
            abname = "default"
        return abname
class Team(models.Model):
    name = models.CharField(max_length=255, null=True)
    structure = models.CharField(max_length=255, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)

class MatchHistory(models.Model):
    team1 = models.ForeignKey(Team, related_name='team1', on_delete=models.CASCADE, null=True)
    score1 = models.IntegerField(null=True)
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    score2 = models.IntegerField(null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(null=True)