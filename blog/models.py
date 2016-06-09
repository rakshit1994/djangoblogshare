from __future__ import unicode_literals
import datetime

from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=140)
	body = models.TextField()
	date = models.DateTimeField('date created', default=datetime.datetime.now())
	username = models.CharField(max_length=140)

	def __str__(self):
		return self.title
