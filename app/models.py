from django.db import models

# Create your models here.


class Tag(models.Model):
    tag = models.CharField(max_length=30)


class Question(models.Model):
    question = models.CharField(max_length=70)
    text = models.TextField()


