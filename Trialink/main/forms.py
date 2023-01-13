from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.core.validators import MaxValueValidator, MinValueValidator

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
		CHOICES3= (('-', '-'),
      			   ('eB01H02122', 'eB01H02122'),
             	   ('eB01L07122', 'eB01L07122'),
				   ('eB03H09122', 'eB03H09122'),
				   ('eB03L14122', 'eB03L14122'),
       			   ('eB05H16122', 'eB05H16122'),
             	   ('eB08H21122', 'eB08H21122'),
				   ('eB01H03112', 'eB01H03112'),
				   ('eB01H03112', 'eB01H03112'),
    			   ('eB01M05112', 'eB01M05112'),
				   ('eB01L06112', 'eB01L06112'),
				   ('eB01L37112', 'eB01L37112'),
				   ('eB03H08112', 'eB03H08112'),
				   ('eB03H10112', 'eB03H10112'),
				   ('eB03M11112', 'eB03M11112'),
				   ('eB03M12112', 'eB03M12112'),
				   )
  
		CHOICES4= (
      				('-', '-'),
             		('P101A', 'P101A'),
               		)
		CHOICES5= (('1', '1+0'),('2', '1+1'),)
  
		scenario= forms.ChoiceField(widget=forms.Select, choices=CHOICES5)
		packet= forms.ChoiceField(widget=forms.Select, choices=CHOICES)
		subscribers= forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2000)])
		server_poc= forms.ChoiceField(widget=forms.Select, choices=CHOICES2)
		enodeb_all= forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)])
		non_telrad_enodeb= forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)])
		add_42U= forms.IntegerField(required=False,validators=[MinValueValidator(0), MaxValueValidator(100)])
		add_7ubox= forms.IntegerField(required=False,validators=[MinValueValidator(0), MaxValueValidator(100)])
		Router= forms.IntegerField(required=False,validators=[MinValueValidator(0), MaxValueValidator(100)])
		add_SGW= forms.IntegerField(required=False,validators=[MinValueValidator(0), MaxValueValidator(10)])
		add_RGW= forms.IntegerField(required=False,validators=[MinValueValidator(0), MaxValueValidator(10)])
		eSFP_10G= forms.IntegerField(required=False,validators=[MinValueValidator(0), MaxValueValidator(100)])
		L2_service= forms.IntegerField(required=False,validators=[MinValueValidator(0), MaxValueValidator(100)])
		bts= forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)])
		bts_type= forms.ChoiceField(widget=forms.Select, choices=CHOICES3)
		terminals= forms.IntegerField(required=False,validators=[MinValueValidator(0), MaxValueValidator(1000)])
		terminals_type= forms.ChoiceField(widget=forms.Select, choices=CHOICES4)


class Test2Form(forms.Form):
	first_name= forms.CharField()
	last_name= forms.CharField()
	email= forms.EmailField()
 
