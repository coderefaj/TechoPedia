from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
	team_name = models.CharField(max_length=40)
	email = models.EmailField(max_length=30,unique=True)
	college = models.CharField(max_length=100)
	phone_no = models.CharField(max_length=10)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username','team_name','college','phone_no']
	def __str__(self):
		return self.email

