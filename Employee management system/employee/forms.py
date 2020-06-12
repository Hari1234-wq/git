from django import forms
from django.contrib.auth.models import User, Group
# from employee.models import *
from django.core.exceptions import ValidationError


class UserForm(forms.ModelForm):
    role = forms.ModelChoiceField(queryset=Group.objects.all())
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    ))



    class Meta:
        model = User
        fields = {'username', 'first_name', 'last_name', 'email', 'role'}


    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            initial = kwargs.setdefault('initial', {})
            if kwargs['instance'].groups.all():
                initial['role'] = kwargs['instance'].groups.all()[0]
            else:
                initial['role'] = None

        forms.ModelForm.__init__(self, *args, **kwargs)

    # def clean_email(self):
    #    if self.cleaned_data['email'].endWith("@hari.com"):
    ##    else:
    #      raise ValidationError("Email id is not valide")

    def save(self):
        password = self.cleaned_data.pop('password')
        role = self.cleaned_data.pop('role')
        u = super().save()
        u.groups.set([role])
        u.set_password(password)
        u.save()
        return u

