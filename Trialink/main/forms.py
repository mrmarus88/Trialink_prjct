from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

 
#class UserForm(forms.Form):
#    login = forms.CharField(label="login")
#    password = forms.CharField(label="password",widget=forms.PasswordInput)
    

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
        
class UserForm(forms.Form):
	packet = forms.CharField(label='packet', max_length= "2" , min_length ="1")
	subscribers = forms.CharField (label='subscribers', max_length="2000", min_length="1")
	enodeball= forms.CharField (label='enodeball', max_length="2000", min_length="1")
	nontelradenodeb= forms.CharField (label='nontelradenodeb', max_length="2000", min_length="1")
	bts= forms.CharField (label='bts', max_length="2000", min_length="1")
	bts_d= forms.CharField (label='bts_d', max_length="2000", min_length="1")
	terminals= forms.CharField (label='terminals', max_length="2000", min_length="1")