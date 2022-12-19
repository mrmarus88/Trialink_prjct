from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(UserRegisterForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
        
class InputForm(forms.Form):
	packet= forms.CharField()
	subscribers= forms.CharField()
	enodeb_all= forms.CharField()
	non_telrad_enodeb= forms.CharField()
	bts= forms.CharField()
	bts_d= forms.CharField()
	terminals= forms.CharField()
 

class Test2Form(forms.Form):
	first_name= forms.CharField()
	last_name= forms.CharField()
	email= forms.EmailField()