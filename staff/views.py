from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Staff


@login_required
def staff_list(request):

    staffs = Staff.objects.all().order_by("full_name")

    return render(
        request,
        "staff/list.html",
        {
            "staffs": staffs,
        },
    )