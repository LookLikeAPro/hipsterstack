from django.db import models

# Create your models here.
class Framework(models.Model):
	name = models.CharField(max_length=200)
	language = models.CharField(max_length=200)
	description = models.CharField(max_length=1000)

class Question(models.Model):
	text = models.CharField(max_length=1000)
	subtitle = models.CharField(max_length=1000)
	mode = (
		('M', 'Multiple Choice'),
		('C', 'Checklist'),
		('R', 'Range'),
	)

class Choice(models.Model):
	question = models.ForeignKey(Question)
