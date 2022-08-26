from django.core import validators
from django import forms
from .models import UniwareMaster, UniwareDimension
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        label = {'email': 'Email'}

class EditProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'is_active']
        label = {'email': 'Email'}



def starts_with_A(value):
 if value[0] != 'A':
  raise forms.ValidationError('Uniware code should start with A')

class FormUniwareMaster(forms.ModelForm):
    uniware = forms.CharField(max_length = 20, required = False) #for extra validators and override other validators
    productpic = forms.ImageField(required = True) #for extra validators and override other validators
    class Meta:
        model = UniwareMaster
        fields = ['uniware','brand','headcat','subcat','productpic']
        # fields = '__all__'
        # exclude =['id']
        labels = {'uniware': 'Uniware','brand': 'Brand','headcat': 'Head Category','subcat':'Sub Category','productpic': 'Product Image'}
        error_message = {
            'productpic':{'required':'Please upload product pic'}
        }
        widgets = {'subcat': forms.PasswordInput
        # 'Uniware': forms.CharField(attrs={'class':'uniware', 'placeholder':'Unicommerce code'}),
        }

class FormUniwareMaster1(forms.Form):
    error_css_class = 'error'
    uniware = forms.CharField(validators=['starts_with_A'], error_messages = {'required': 'Please enter uniware code'})
    brand = forms.CharField(label= 'Brand', error_messages = {'required': 'Please enter brand'})
    headcat = forms.CharField(label='Head Category', error_messages = {'required': 'Please enter head category'}, min_length = 2, max_length = 50)
    subcat = forms.CharField(label='Sub Category', widget=forms.PasswordInput, error_messages = {'required': 'Please enter sub category'})
    productpic = forms.ImageField(label='Product Picture', error_messages = {'required': 'Please enter sub category'})

class FormUniwareDimension(forms.ModelForm):
    class Meta:
        model = UniwareDimension
        fields = '__all__'