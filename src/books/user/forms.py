from user.models import User
from user.tasks import send_email_async

from django import forms
from django.forms import ModelForm
# from django.forms import ModelForm

from . import models


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone')


class ContactUsForm(forms.Form):
    subject = forms.CharField()
    text = forms.CharField()

    def save(self):
        subject = self.cleaned_data['subject']
        text = self.cleaned_data['text']
        send_email_async.delay(subject, text)


class ContactUs(ModelForm):
    class Meta:
        model = models.Contact
        fields = ['subject', 'text']
