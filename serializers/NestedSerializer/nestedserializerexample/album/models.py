from django.db import models

# Create your models here.
class Singer(models.Model):
	name = models.CharField(max_length=100)
	gender = models.CharField(max_length=100)

class Song(models.Model):
	title = models.CharField(max_length=100)
	singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name="sung")
	duration = models.IntegerField()