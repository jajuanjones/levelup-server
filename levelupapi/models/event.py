from datetime import date
from time import time
from tkinter import CASCADE
from django.db import models

from levelupapi.models import game

class Event(models.Model):
    """This class will create an instance of an event object
    """
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    # why do we include a string parameter in foreign key
        # to reference another model
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    attendees = models.ManyToManyField("Gamer", related_name="gamers")
    
    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value