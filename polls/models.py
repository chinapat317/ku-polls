import datetime
from msilib.schema import Class
from operator import mod
from time import timezone
from django.db import models
from django.utils import timezone

class Question(models.Model):

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published')

    def was_publish_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text