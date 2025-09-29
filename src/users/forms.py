from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
User = get_user_model()

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': _('Enter your email')  # سيتم ترجمته تلقائيًا
        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': _('Enter your username')
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': _('Enter your password')
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': _('Confirm your password')
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
