from django.contrib.auth.forms import AuthenticationForm

from .models import ServiceUser


class ServiceUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(ServiceUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = ServiceUser
        fields = ("username", "password")