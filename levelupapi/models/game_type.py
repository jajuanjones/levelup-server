from django.db import models

class GameType(models.Model):
    """This class will create an instance of a game type object
    """
    label = models.CharField(max_length=20)