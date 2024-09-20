from django.db import models

# Create your models here.


class UserL(models.Model):
    status_choice =[
        ('offline', 'Offline'),
        ('online' , 'Online'),
        ('solo' , 'Solo'),
        ('lobby', 'Lobby'),
        ('ingame', 'In Game'),
    ]
    
    name = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    status = models.CharField(max_length=7, choices=status_choice, default='offline')

    def __str__(self):
        return self.name
    
class RoomL(models.Model):
    room_type = [
        ('soloai', 'Adventure'),
        ('offline', 'Challenge'),
        ('online', 'multiOn'),
        ('tournament', 'Tournament'),
    ]
    name = models.CharField(max_length=50, blank=False, null=False)
    playerNbr = models.IntegerField(default=2)
    type = models.CharField(max_length=10, choices = room_type)
    players = models.ManyToManyField(UserL, related_name='rooms', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def is_full(self):
        return self.players.count() >= self.playerNbr
    
    def get_player_names(self):
        return [player.name for player in self.players.all()]