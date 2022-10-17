from django.db import models

# Create your models here.
#model for each game
class Game(models.Model):
    #save the initial status of the game
    initial_status = models.JSONField(default=dict)
    winner = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    
    


