from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta

from .forms import AttendanceForm
from .models import Attendance
from members.models import Member


@login_required
def attendance(request):

    message = ""
    success = False

    if request.method == "POST":

        form = AttendanceForm(request.POST)

        if form.is_valid():

            member_id = form.cleaned_data["member_id"]

            try:
                member = Member.objects.get(member_id=member_id)

            except Member.DoesNotExist:

                return render(
                    request,
                    "attendance/index.html",
                    {
                        "form": form,
                        "message": "❌ Invalid Member ID",
                        "success": False,
                    },
                )

            now = timezone.now()

            last = Attendance.objects.filter(
                member=member
            ).order_by("-entry_time").first()

            if last:

                if (
                    last.status == "Inside"
                    and last.exit_time is None
                ):

                    last.exit_time = now
                    last.status = "Exited"
                    last.save()

                    message = (
                        f"👋 Goodbye {member.full_name}. Exit marked successfully."
                    )

                    success = True

                elif now - last.entry_time < timedelta(hours=12):

                    message = (
                        "⚠️ Attendance already marked in the last 12 hours."
                    )

                    success = False

                else:

                    Attendance.objects.create(member=member)

                    message = (
                        f"✅ Welcome {member.full_name}. Entry marked successfully."
                    )

                    success = True

            else:

                Attendance.objects.create(member=member)

                message = (
                    f"✅ Welcome {member.full_name}. Entry marked successfully."
                )

                success = True

    else:

        form = AttendanceForm()

    return render(
        request,
        "attendance/index.html",
        {
            "form": form,
            "message": message,
            "success": success,
        },
    )