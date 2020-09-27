from user.models import User

from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone')
