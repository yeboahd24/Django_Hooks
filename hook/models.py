from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django_lifecycle import LifecycleModel, hook, AFTER_SAVE, AFTER_CREATE

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
        
        # Save username and email to User model

	@hook(AFTER_SAVE)
	def create_user_after_creating_profile(self):
		User.objects.create(username=self.name, email=self.email)

	# Send email to user after creating profile
	# Subject = "Account created"
	# body = "You have created your account successfully"
	# from = self.email
	# to = "yeboahd24@gmail.com"

	@hook(AFTER_CREATE)
	def send_mail_after_creating_profile(self):
		send_mail(
				"Account created", "You have created your account successfully",
				self.email, ["yeboahd24@gmail.com"]
				)

