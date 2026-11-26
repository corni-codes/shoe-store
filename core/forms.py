from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Order


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'password1',
            'password2'
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if CustomUser.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("This phone number is already in use.")
        return phone_number


class CheckoutForm(forms.Form):

    full_name = forms.CharField(max_length=150)

    phone_number = forms.CharField(max_length=15)

    email = forms.EmailField()

    address = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3})
    )

    city = forms.CharField(max_length=100)

    state = forms.CharField(max_length=100)
