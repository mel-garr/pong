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
    typel = models.CharField(max_length=10, choices = room_type ,default='none')

    def __str__(self):
        return self.name



class playerData(models.Model):
    paddle_type = [
    ('default', 'Default'),
    ('type1', 'Type 1'),
    ('type2', 'Type 2'),
    ]

    ball_type = [
    ('default', 'Default'),
    ('type1', 'Type 1'),
    ('type2', 'Type 2'),
    ]

    field_type = [
    ('default', 'Default'),
    ('type1', 'Type 1'),
    ('type2', 'Type 2'),
    ]

    name = models.CharField(max_length=50, blank=False, null=False)
    uniq_id = models.CharField(max_length=50, blank=True, null=True) # in case of online games ignore it for the moment
    paddle = models.CharField(max_length=50, choices= paddle_type, default='default')
    ball = models.CharField(max_length=50, choices= ball_type, default='default')
    field = models.CharField(max_length=50, choices= field_type, default='default')
    

    def __str__(self):
        return str(self.id)

        


class roomData(models.Model):
    room_type = [
    ('soloai', 'Adventure'),
    ('offline', 'Challenge'),
    ('online', 'multiOn'),
    ('tournament', 'Tournament'),
    ]

    status_choice =[
    ('gamestart', 'Game Start'),
    ('pause', 'Pause'),
    ('ended', 'Ended'),
    ('inprogress', 'In Progress'),
    ]
    
    team = [
    ('tie', 'Tie'),
    ('blue', 'Blue'),
    ('red', 'Red'),
    ]

    name = models.CharField(max_length=50, blank=False, null=False)
    uniq_id = models.CharField(max_length=50, blank=True, null=True)
    gametype = models.CharField(max_length=10, choices = room_type ,default='offline')
    gamestatus = models.CharField(max_length=10, choices = status_choice ,default='gamestart')
    winning_team = models.CharField(max_length=10, choices = team ,default='tie')
    max_score = models.IntegerField(default=2)

    redteamplayers = models.ManyToManyField(playerData, related_name='red_team')
    redteamScore = models.IntegerField(default=0)

    blueteamplayers = models.ManyToManyField(playerData, related_name='blue_team')
    blueteamScore = models.IntegerField(default=0)
    

    def __str__(self):
        return str(self.id)