from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    phone_number = forms.CharField(required=False, label='Номер телефона', max_length=15)
    bio = forms.CharField(required=False, label='О себе', widget=forms.Textarea(attrs={'rows': 3}))
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'bio', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        user.bio = self.cleaned_data['bio']
        if commit:
            user.save()
        return user 