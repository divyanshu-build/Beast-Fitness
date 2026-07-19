from django.shortcuts import render
from members.models import Member
from payments.models import Payment
from attendance.models import Attendance
from django.utils import timezone
from django.db.models import Sum
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):

    total_members = Member.objects.count()

    total_collection = (
        Payment.objects.aggregate(total=Sum("amount"))["total"] or 0
    )

    today = timezone.localdate()

    # Collection
    today_collection = (
        Payment.objects.filter(payment_date=today)
        .aggregate(total=Sum("amount"))["total"] or 0
    )

    # Attendance
    today_attendance = Attendance.objects.filter(
        attendance_date=today
    ).count()

    inside_gym = Attendance.objects.filter(
        status="Inside"
    ).count()

    # Due Members
    overdue_members = Member.objects.filter(
        next_due_date__lt=today
    ).count()

    due_today = Member.objects.filter(
        next_due_date=today
    ).count()

    due_members = overdue_members + due_today

    # Recent Data
    recent_members = Member.objects.order_by("-id")[:5]

    recent_payments = Payment.objects.order_by("-payment_date")[:5]

    recent_due_members = Member.objects.filter(
        next_due_date__lte=today
    ).order_by("next_due_date")[:5]

    # Status for each due member
    for member in recent_due_members:

        if member.next_due_date < today:
            member.display_status = "Overdue"

        elif member.next_due_date == today:
            member.display_status = "Due Today"

        else:
            member.display_status = "Paid"

    context = {
        "total_members": total_members,
        "total_collection": total_collection,
        "today_collection": today_collection,
        "today_attendance": today_attendance,
        "inside_gym": inside_gym,
        "due_members": due_members,
        "overdue_members": overdue_members,
        "due_today": due_today,
        "recent_members": recent_members,
        "recent_payments": recent_payments,
        "recent_due_members": recent_due_members,
    }

    return render(request, "dashboard.html", context)