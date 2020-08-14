from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=258)
    def __str__(self):
        return self.name+','+self.password

class Score(models.Model):
    user_name = models.CharField(max_length=128)
    png_path = models.CharField(max_length=258)
    wav_path = models.CharField(max_length=258)
    json_path = models.CharField(max_length=258)
    score_name = models.CharField(max_length=258)
    def __str__(self):
        return self.user_name+','+self.score_name+','+self.png_path+','+self.wav_path
