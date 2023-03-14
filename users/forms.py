from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from app.models import Profile

class CreateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'facebook_url', 'insta_url', 'linkedin_url', 'github_url')
        widgets = {
            'bio': forms.Textarea(attrs={'class':'form-control'}),
            'profile_pic':forms.FileInput(attrs={'class':'form-control'}),
            'facebook_url':forms.TextInput(attrs={'class':'form-control'}),
            'insta_url':forms.TextInput(attrs={'class':'form-control'}),
            'linkedin_url':forms.TextInput(attrs={'class':'form-control'}),
            'github_url':forms.TextInput(attrs={'class':'form-control'}),
        }


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'facebook_url', 'insta_url', 'linkedin_url', 'github_url')
        widgets = {
            'bio': forms.Textarea(attrs={'class':'form-control'}),
            'profile_pic':forms.FileInput(attrs={'class':'form-control'}),
            'facebook_url':forms.TextInput(attrs={'class':'form-control'}),
            'insta_url':forms.TextInput(attrs={'class':'form-control'}),
            'linkedin_url':forms.TextInput(attrs={'class':'form-control'}),
            'github_url':forms.TextInput(attrs={'class':'form-control'}),
        }


class ManualChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="Old Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label="New Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('old_password', 'new_ppassword1', 'new_password2')


class SignupForm(UserCreationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(label="Email", widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')


class ProfileEditForm(UserChangeForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')