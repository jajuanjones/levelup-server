from turtle import ondrag
from django.db import models

from levelupapi.models import game_type

class Game(models.Model):
    """This class will create an instance of a game object
    """
    SKILL_LEVELS = [
        (1, 'Easy',),
        (2, 'Medium',),
        (3, 'Hard',),
        (4, 'Ultra',)
    ]
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    maker = models.CharField(max_length=20)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    number_of_players = models.IntegerField()
    skill_level = models.CharField(max_length=6, choices=SKILL_LEVELS)