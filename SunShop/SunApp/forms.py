from django import forms
# from .models import PurchaseRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PurchaseRequest

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

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].label = 'First Name'

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['last_name'].label = 'Last Name'


# Create Add Request Form
class AddRequestForm(forms.ModelForm):
    requested_by = forms.ModelChoiceField(queryset=User.objects.all(), label='Requested By', widget=forms.Select(attrs={'placeholder': 'Username','class': 'form-control'}))
    item_name = forms.CharField(max_length=200, label='Item Name', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Item Name'}))
    vendor = forms.CharField(max_length=200, label='Vendor', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Vendor'}))
    quantity = forms.IntegerField(label='Quantity', widget=forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Quantity'}))
    price = forms.DecimalField(label='Price', widget=forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Price'}))
    purchase_link = forms.URLField(label='Purchase Link', widget=forms.URLInput(attrs={'class': 'form-control','placeholder': 'Purchase Link'}))
    project = forms.CharField(max_length=200, label='Project', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Project'}))
    notes = forms.CharField(label='Notes', widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'Notes'}))

    class Meta:
        model = PurchaseRequest
        fields = ('requested_by', 'project', 'item_name', 'vendor', 'quantity', 'price', 'purchase_link', 'notes')