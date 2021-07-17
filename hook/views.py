from django.shortcuts import render
from django.http import HttpResponse

from .forms import RegistrationForm

def registration(request):

	if request.method == 'POST':
		profile = RegistrationForm(request.POST)
		profile.name = request.POST.get('name', '')
		profile.surname = request.POST.get('surname', '')
		profile.phone_number = request.POST.get('phone', '')
		profile.email = request.POST.get('email', '')
		profile.education = request.POST.get('education', '')
		profile.country = request.POST.get('country', '')
		profile.state = request.POST.get('state', '')

		if profile.is_valid():
			profile.save()
			return HttpResponse("Save successfully")

		return HttpResponse("Invalid form")

	else:
		profile = RegistrationForm()
	return render(request, 'index.html', {'profile':profile})
