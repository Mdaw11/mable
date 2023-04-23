from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    account_type = forms.ChoiceField(choices=CustomUser.ACCOUNT_TYPE_CHOICES)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        
    # saves the account_type once a user registers
    def save(self, commit=True):
        user = super().save(commit=False)
        user.account_type = self.cleaned_data['account_type']
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic']

