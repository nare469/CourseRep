from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
	code=models.CharField(max_length=10, db_index=True)
	name=models.CharField(max_length=20)
	description=models.TextField()
	users = models.ManyToManyField(User)

class Topic(models.Model):
	name=models.CharField(max_length=30)
	course = models.ForeignKey(Course)

class Resource(models.Model):
	title=models.CharField(max_length=30)
	content=models.TextField()
	points=models.IntegerField()
	viewcount=models.IntegerField()
	author=models.ForeignKey(User)
	topic=models.ForeignKey(Topic)


class Vote(models.Model):
	voter=models.ForeignKey(User)
	resource=models.ForeignKey(Resource)
	value=models.IntegerField()
