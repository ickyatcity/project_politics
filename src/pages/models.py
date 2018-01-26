# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.urls import reverse
from django.db import models
from django.db.models import F
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Candidate(models.Model): 
	id_candidate = models.CharField(max_length=32, unique=True)
	userId = models.ForeignKey(settings.AUTH_USER_MODEL)
	name_candidate = models.CharField(max_length=60, unique=False)
	summary = models.TextField(max_length=500)
	descriptions = models.TextField(max_length=2000)
	slug = models.SlugField(unique=True)
	timestamp = models.DateTimeField(auto_now_add = True)
	# candidate_pic = models.ImageField(upload_to=None, default=None)


	def __str__(self):
		return self.name_candidate
	
	def get_absolute_url(self):
		return reverse("candidate:detailcandidate", kwargs={"pk":self.pk})	

	def save(self, *args, **kwargs):
            self.slug = slugify(self.name_candidate)
	    super(Candidate, self).save(*args, **kwargs)		


        class Meta:
			# https://docs.djangoproject.com/en/2.0/ref/models/options/
		#  order_with_respect_to = 'id_candidate'
		#  ordering = [F('id_candidate').asc(nulls_last=True)]
		   ordering = ["-timestamp", "id_candidate" ]
# This is a validation for the field - if a specific validation is needed its lecture 19
        # def clean(self, *args, **kwrgs): 
        #      name_candidate = self.name_candidate
        #      if name_candidate == "abc":
        #          raise forms.ValidationError("Cannot be testfield ")
        #      return super(Candidate, self).clean(*args, **kwrgs)



class CandidateAchivement(models.Model):
	id_candidate_achivement = models.ForeignKey(Candidate, related_name = 'achivement')
	achivement1 = models.TextField(max_length=500)
	achivement2 = models.TextField(max_length=500)
	achivement3 = models.TextField(max_length=500)
	achivement4 = models.TextField(max_length=500)
	achivement5 = models.TextField(max_length=500)

class CandidateScore(models.Model):
    id_candidate_score = models.ForeignKey(Candidate, related_name = 'score')
    score = models.IntegerField()
    userId = models.ForeignKey(User, related_name = 'score')


class Reviews(models.Model):
	userId = models.ForeignKey(settings.AUTH_USER_MODEL)
	id_candidate_reivew = models.ForeignKey(Candidate, related_name = 'reviews')
	header = models.CharField(max_length=500, unique=True)
	review = models.CharField(max_length=500, unique=True)
	date_of_review = models.DateTimeField(auto_now_add = True)





