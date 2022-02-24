from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Newuser
from django import forms


class login_form(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


GEEKS_CHOICES =(
    ("1", "Doctor"),
    ("2", "Patient"),
)
class signup_form(UserCreationForm): 
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    Group = [('Doctor', 'Doctor'), ('Patient', 'Patient'),]
    groups = forms.ChoiceField(choices=Group)
    
    class Meta:
        model = Newuser
        fields = ['username', 'first_name', 'last_name', 'profilepic', 'email','address']
        labels={'first_name': 'First Name','last_name': 'Last Name','profilepic': 'Profile Picture ','email':'Email ID', 'confrompass':'Confirm Password', "usertype": 'User type  '}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        'address':forms.TextInput(attrs={'class':'form-control'}),
        }
