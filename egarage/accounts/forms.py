from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#we are extending the UserCreationForm and adding the email field
# the name of our form is now SignUpForm
# class Meta tells Django which model should be used to create the Form
# the User model has various input fields so you call the ones you need

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254,required=True,widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username','email','password','password2')
