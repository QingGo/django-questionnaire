import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class Questionnaire(models.Model):
    questionnaire_name = models.CharField(max_length=200)
    detail_info = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.questionnaire_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'published recently'

class Question(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text