from django import forms
from .models import Payment


class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment

        fields = [
            "member",
            "amount",
            "payment_mode",
            "received_by",
            "remarks",
        ]

        widgets = {

            "member": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "amount": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Amount"
                }
            ),

            "payment_mode": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "received_by": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "remarks": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Remarks (Optional)"
                }
            ),

        }