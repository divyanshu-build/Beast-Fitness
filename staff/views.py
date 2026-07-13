from django.shortcuts import render, redirect
from .models import Payment
from .forms import PaymentForm


def payment_list(request):

    if request.method == "POST":

        form = PaymentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("payments")

    else:
        form = PaymentForm()

    payments = Payment.objects.select_related("member").order_by("-id")

    return render(
        request,
        "payments/list.html",
        {
            "payments": payments,
            "form": form,
        },
    )