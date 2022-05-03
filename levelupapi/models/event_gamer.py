from django.db import models 

class EventGamer(models.Model):
    """This class will create an instance of an event gamer
    """
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)