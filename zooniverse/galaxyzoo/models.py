from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published',blank=True,null=True)
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
	    now = timezone.now()
	    return now - datetime.timedelta(days=1) <= self.pub_date <= now

@python_2_unicode_compatible
class Parent(models.Model):
    question_text = models.CharField(max_length=200)
    hint = models.CharField(max_length=200,blank=True)
    answer = models.BooleanField()
    pub_date = models.DateTimeField('date published',blank=True,null=True)
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

@python_2_unicode_compatible
class Round(models.Model):
    question_text = models.CharField(max_length=200)
    hint = models.CharField(max_length=200,blank=True)
    answer = models.BooleanField()
    pub_date = models.DateTimeField('date published',blank=True,null=True)
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

@python_2_unicode_compatible
class Edge(models.Model):
    question_text = models.CharField(max_length=200)
    hint = models.CharField(max_length=200,blank=True)
    answer = models.BooleanField()
    pub_date = models.DateTimeField('date published',blank=True,null=True)
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

@python_2_unicode_compatible
class Bulge(models.Model):
    question_text = models.CharField(max_length=200)
    hint = models.CharField(max_length=200,blank=True)
    answer = models.BooleanField()
    pub_date = models.DateTimeField('date published',blank=True,null=True)
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

@python_2_unicode_compatible
class Bar(models.Model):
    question_text = models.CharField(max_length=200)
    hint = models.CharField(max_length=200,blank=True)
    answer = models.BooleanField()
    pub_date = models.DateTimeField('date published',blank=True,null=True)
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

@python_2_unicode_compatible
class Pattern(models.Model):
    question_text = models.CharField(max_length=200)
    hint = models.CharField(max_length=200,blank=True)
    answer = models.BooleanField()
    pub_date = models.DateTimeField('date published',blank=True,null=True)
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

@python_2_unicode_compatible
class Sa(models.Model):
    question_text = models.CharField(max_length=200)
    hint = models.CharField(max_length=200,blank=True)
    answer = models.BooleanField()
    pub_date = models.DateTimeField('date published',blank=True,null=True)
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

@python_2_unicode_compatible
class Sa_num(models.Model):
    question_text = models.CharField(max_length=200)
    hint = models.CharField(max_length=200,blank=True)
    answer = models.BooleanField()
    pub_date = models.DateTimeField('date published',blank=True,null=True)
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

@python_2_unicode_compatible
class Prominence(models.Model):
    question_text = models.CharField(max_length=200)
    hint = models.CharField(max_length=200,blank=True)
    answer = models.BooleanField()
    pub_date = models.DateTimeField('date published',blank=True,null=True)
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

@python_2_unicode_compatible
class Tidal(models.Model):
    question_text = models.CharField(max_length=200)
    hint = models.CharField(max_length=200,blank=True)
    answer = models.BooleanField()
    pub_date = models.DateTimeField('date published',blank=True,null=True)
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

@python_2_unicode_compatible
class Odd(models.Model):
    question_text = models.CharField(max_length=200)
    hint = models.CharField(max_length=200,blank=True)
    answer = models.BooleanField()
    pub_date = models.DateTimeField('date published',blank=True,null=True)
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.question_text

