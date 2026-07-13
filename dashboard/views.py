from django.shortcuts import render
from members.models import Member
from payments.models import Payment
from django.db.models import Sum
from django.utils import timezone


def dashboard(request):

    total_members = Member.objects.count()

    total_payments = Payment.objects.count()

    total_collection = (
        Payment.objects.aggregate(total=Sum("amount"))["total"] or 0
    )

    today = timezone.now().date()

    todays_payments = Payment.objects.filter(
        payment_date=today
    ).count()

    recent_members = Member.objects.order_by("-id")[:5]

    recent_payments = Payment.objects.select_related(
        "member"
    ).order_by("-id")[:5]

    context = {
        "total_members": total_members,
        "total_payments": total_payments,
        "total_collection": total_collection,
        "todays_payments": todays_payments,
        "recent_members": recent_members,
        "recent_payments": recent_payments,
    }

    return render(request, "dashboard.html", context)