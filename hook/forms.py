from django import forms
from .models import Profile

class RegistrationForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = "__all__"