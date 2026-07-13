from django import forms
from .models import Payment


class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment

        fields = [
            "member",
            "amount",
            "payment_mode",
            
        ]

        widgets = {

            "member": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "amount": forms.NumberInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "payment_mode": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "next_due_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),

        }