from django.shortcuts import render
from members.models import Member
from payments.models import Payment
from attendance.models import Attendance
from django.utils import timezone
from django.db.models import Sum

def dashboard(request):

    total_members = Member.objects.count()

    total_collection = (
        Payment.objects.aggregate(total=Sum("amount"))["total"] or 0
    )

    today = timezone.localdate()

    today_attendance = Attendance.objects.filter(
        attendance_date=today
    ).count()

    inside_gym = Attendance.objects.filter(
        status="Inside"
    ).count()

    recent_members = Member.objects.order_by("-id")[:5]

    recent_payments = Payment.objects.order_by("-payment_date")[:5]

    context = {
        "total_members": total_members,
        "total_collection": total_collection,
        "today_attendance": today_attendance,
        "inside_gym": inside_gym,
        "recent_members": recent_members,
        "recent_payments": recent_payments,
    }

    return render(request, "dashboard.html", context)