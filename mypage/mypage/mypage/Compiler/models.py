from __future__ import unicode_literals

from django.db import models

class Compiler(models.Model):
	txt = models.TextField(max_length="300",default='none')



	def __str__(self):
		return u'Program : %s' % (self.txt)
