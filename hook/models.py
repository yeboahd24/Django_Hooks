from django.db import models
from django.contrib.auth.models import User

from django_lifecycle import LifecycleModel, hook, AFTER_SAVE

class Profile(LifecycleModel, models.Model):

	name = models.CharField(max_length=100, blank=True)
	surname = models.CharField(max_length=100, blank=True)
	phone_number = models.CharField(max_length=100, blank=True)
	address = models.CharField(max_length=100, blank=True)
	email = models.EmailField(max_length=100, blank=True)
	education = models.CharField(max_length=100, blank=True)
	country = models.CharField(max_length=100, blank=True)
	state = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return self.name


	@hook(AFTER_SAVE)
	def create_user_after_creating_profile(self):
		User.objects.create(username=self.name, email=self.email)