from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            "full_name",
            "phone",
            "gender",
            "age",
            "address",
            "membership",
        ]

        widgets = {
            "full_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Full Name"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Contact Number"
            }),

            "gender": forms.Select(attrs={
                "class": "form-select"
            }),

            "age": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "address": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3
            }),

            "membership": forms.Select(attrs={
                "class": "form-select"
            }),
        }