from django.db import models
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class UserProfile(models.Model): 
    user = models.OneToOneField(User)
    happy_ratio = models.FloatField()
   


class Highs(models.Model):
	description = models.TextField(max_length=250)
	user = models.ForeignKey(User)

	def __str__(self):
		return self.description

class Lows(models.Model):
	description = models.TextField(max_length=250)
	user = models.ForeignKey(User)

	def __str__(self):
		return self.description

class Dealbreakers(models.Model):
	flags = models.IntegerField()
	description = models.CharField(max_length=128)
	user = models.ForeignKey(User)

	def __str__(self):
		return self.flags
		return self.description

