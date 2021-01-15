from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm

from .models import ServiceUser


class ServiceUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(ServiceUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = ServiceUser
        fields = ("username", "password")

class ServiceUserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(ServiceUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""

    def clean_age(self):
        data = self.cleaned_data["age"]
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")
        return data

    class Meta:
        model = ServiceUser
        fields = ("username", "first_name", "password1", "password2", "email", "age", "avatar")


class ServiceUserEditForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(ServiceUserEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""

    def clean_age(self):
        data = self.cleaned_data["age"]
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")

        return data

    class Meta:
        model = ServiceUser
        fields = ("username", "first_name", "email", "age", "avatar")