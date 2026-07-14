from django.shortcuts import render
from .models import Staff


def staff_list(request):

    staffs = Staff.objects.all().order_by("full_name")

    return render(
        request,
        "staff/list.html",
        {
            "staffs": staffs,
        },
    )