from django import forms
from django.contrib.auth.forms import UserCreationForm

from myapp.models import Order, Student, Course
from myapp.models import Review


class SearchForm(forms.Form):
    LENGTH_CHOICES = [
        (8, '8 Weeks'),
        (10, '10 Weeks'),
        (12, '12 Weeks'),
        (14, '14 Weeks'),
    ]
    name = forms.CharField(max_length=100, required=False, label="Student Name")
    length = forms.TypedChoiceField(widget=forms.RadioSelect, choices=LENGTH_CHOICES, coerce=int, required=False,
                                    label="Preferred course duration")
    max_price = forms.IntegerField(min_value=0, label="Maximum Price")


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['courses', 'student', 'order_status']
        widgets = {'courses': forms.CheckboxSelectMultiple(), 'order_type': forms.RadioSelect}
        labels = {'student': u'Student Name', }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['reviewer','course','rating','comments']
        widgets = {'course' : forms.RadioSelect}
        labels = {'reviewer' : u'Please enter a valid email','rating':u'Rating: An integer between 1 (worst) and 5 (best)',}

class loginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class PasswordForm(forms.Form):
    username = forms.CharField( required=True, label='Username')
    email = forms.CharField( required=True, label='Email')

class RegisterForm(UserCreationForm):
 def __init__(self, *args, **kwargs):
  super(RegisterForm, self).__init__(*args, **kwargs)
  # do not require password confirmation
  del self.fields['password2']

 class Meta:
  model = Student
  fields = ['username', 'first_name', 'last_name', 'province', 'interested_in']

  widgets = {
   'interested_in': forms.CheckboxSelectMultiple,
  }

  labels = {
   'first_name': 'First Name',
   'last_name': 'Last Name',
   'interested_in': 'Interested In'
  }

