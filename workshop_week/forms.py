from django import forms

from .models import Workshop


class ProposeForm(forms.ModelForm):

    class Meta:
        model = Workshop
        fields = ('title', 'description', 'know_or_bring', 'category',)
