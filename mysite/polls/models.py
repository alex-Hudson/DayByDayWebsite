import datetime

from django.db import models
from django.utils import timezone

class Series(models.Model):
    series_title = models.CharField(max_length=200, default='add series title', null=True, blank=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.series_title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Question(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE, blank=True, null=True, default='')
    question_text = models.CharField(max_length=200, null=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, blank=True)
    passage_text = models.CharField(max_length=1000, blank=True)
    day_by_day_question_text = models.CharField(max_length=1000, blank=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
