from django import forms

class AttendanceForm(forms.Form):

    member_id = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Enter Member ID (BF0001)"
            }
        )
    )