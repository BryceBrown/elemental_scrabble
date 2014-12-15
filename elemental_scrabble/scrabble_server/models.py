from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

# Create your models here.
class UserExt(models.Model):
    SUPPORTED_LANGUAGES = (
        (0, 'English'),
    )
    User = models.OneToOneField(User, related_name='ExtUser')
    Language = models.IntegerField(choices=SUPPORTED_LANGUAGES)


class Game(models.Model):
    CURRENT_PLAYER = (
        (0, 'NA'),
        (1, 'Player One'),
        (2, 'Player Two')
    ) 
    PlayerOne = models.ForeignKey(User, related_name='GamesChallenged')
    PlayerTwo = models.ForeignKey(User, related_name='ChallengesAccepted')
    Accepted = models.BooleanField(default=False)
    FirstPlayer = models.IntegerField(choices=CURRENT_PLAYER, default=0)

class Tile(models.Model):
    TileLetter = models.CharField(max_length=1)
    TilePointValue = models.IntegerField()

class GameTiles(models.Model):
    Tile = models.ForeignKey(Tile)
    Game = models.ForeignKey(Game)
    X = models.IntegerField()
    Y = models.IntegerField()
    Owner = models.ForeignKey(User)
    Round = models.IntegerField()

class GameWords(models.Model):
    Game = models.ForeignKey(Game)
    Word = models.CharField(max_length=20)
    PointValue = models.IntegerField()
    RoundPlayed = models.IntegerField()

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = ExtUser.objects.get_or_create(User=instance)
       Token.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User) 