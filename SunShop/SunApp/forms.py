from django import forms
# from .models import PurchaseRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'First Name'}) )
    last_name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Last Name'}))
    email = forms.EmailField(max_length=200, label='Email', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Email Address'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = 'Username'
        self.fields['username'].help_text = 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = 'Password'
        self.fields['password1'].help_text = 'Your password must contain at least 8 characters.'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = 'Confirm Password'
        self.fields['password2'].help_text = 'Enter the same password as before, for verification.'

        # self.fields['first_name'].widget.attrs['class'] = 'form-control'
        # self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        # self.fields['first_name'].label = 'First Name'
        # self.fields['first_name'].help_text = 'Required. 30 characters or fewer.'

        # self.fields['last_name'].widget.attrs['class'] = 'form-control'
        # self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        # self.fields['last_name'].label = 'Last Name'
        # self.fields['last_name'].help_text = 'Required. 30 characters or fewer.'


# class PurchaseRequestForm(forms.ModelForm):
#     class Meta:
#         model = PurchaseRequest
#         fields = ['item_name', 'purchase_link', 'price', 'project', 'notes']
