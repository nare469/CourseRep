from django.db import models

class User(models.Model):
	username = models.CharField(max_length=20, db_index=True)
	first_name = models.CharField(max_length=20)
	last_name=models.CharField(max_length=20)
	password=models.CharField(max_length=20)

class Course(models.Model):
	code=models.CharField(max_length=10, db_index=True)
	name=models.CharField(max_length=20)
	description=models.TextField()
	users = models.ManyToManyField(User, through='Subscription')

class Topic(models.Model):
	name=models.CharField(max_length=30)
	course = models.ForeignKey(Course)

class Resource(models.Model):
	content=models.TextField()
	points=models.IntegerField()
	viewcount=models.IntegerField()
	author=models.ForeignKey(User)
	topic=models.ForeignKey(Topic)

class Subscription(models.Model):
	user=models.ForeignKey(User)
	course=models.ForeignKey(Course)

class Vote(models.Model):
	voter=models.ForeignKey(User)
	resource=models.ForeignKey(Resource)
	value=models.IntegerField()