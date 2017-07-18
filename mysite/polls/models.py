from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Question(models.Model):
    """
    Database table to include questions associated with the app.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        """
        The text that appears in the object represented
        """
        return self.question_text
    def was_published_recently(self):
        """Determine if the question was published in the last day."""
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    """
    Database table to include responses to each question.  One question can have many choices.  Questions are delegated by a foreign key.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

   
