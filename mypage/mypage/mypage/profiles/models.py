from __future__ import unicode_literals

from django.db import models

# Create your models here.
class profile(models.Model):
	name = models.CharField(max_length=128)
	description = models.TextField(default='description default text')
	location = models.CharField(max_length=128 , default='my location',blank=True,null=True)
	job = models.CharField(max_length=128 , null=True)


	def __unicode__(self):
		return self.name

class course_name(models.Model):
	title = models.CharField(max_length=128)
	content = models.TextField(default="Welcome to the course")
	url = models.CharField(max_length=128)
	img_url = models.CharField(max_length=128)


	def __unicode__(self):
		return self.title
