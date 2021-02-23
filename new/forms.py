from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


class AddCodeForm(forms.Form):
    row_code = forms.CharField()

    @property
    def clean_new_code(self):
        code = self.data['row_code']

        if code == "":
            raise ValidationError(_('Invalid text code - text code is empty'))

        return code


class ViewCodeForm(forms.Form):
    view_code = forms.CharField()

    @property
    def clean_view_code(self):
        code = self.data['row_code']

        if code == "":
            raise ValidationError(_('Invalid text code - text code is empty'))

        return code

