from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User





class NewUserForm(UserCreationForm):
	username = forms.CharField(
    label = 'E-Mail', #username in persion
    required = True,
)  
      
	class Meta:
		model = User
		fields = ("username", "password1", "password2")
	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

