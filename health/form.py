from django import forms
from .models import Appointment
from .models import Contact

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

# class RegistrationForm(UserCreationForm):

    # class Meta:
    #     model = User 
    #     fields = ['username', 'email', 'password1', 'password2']