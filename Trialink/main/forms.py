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
		CHOICES= (('1', 'Packet 1'),('2', 'Packet 2'),)
		CHOICES2= (('RONET 300', 'RONET Compact pro 300'),('RONET 500', 'RONET Compact pro 500'),('RONET Professional', 'RONET Professional'),)
		packet= forms.ChoiceField(widget=forms.Select, choices=CHOICES)
		subscribers= forms.CharField()
		server_poc= forms.ChoiceField(widget=forms.Select, choices=CHOICES2)
		enodeb_all= forms.CharField()
		non_telrad_enodeb= forms.CharField()
		add_42U= forms.CharField(required=False)
		add_7ubox= forms.CharField(required=False)
		Router= forms.CharField(required=False)
		add_SGW= forms.CharField(required=False)
		add_RGW= forms.CharField(required=False)
		eSFP_10G= forms.CharField(required=False)
		L2_service= forms.CharField(required=False)
		bts= forms.CharField()
		bts_D= forms.CharField(required=False)
		terminals= forms.CharField(required=False)


class Test2Form(forms.Form):
	first_name= forms.CharField()
	last_name= forms.CharField()
	email= forms.EmailField()