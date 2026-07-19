from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Member
from .forms import MemberForm
from payments.models import Payment
from attendance.models import Attendance


@login_required
def member_list(request):

    if request.method == "POST":
        form = MemberForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("members")

    else:
        form = MemberForm()

    members = Member.objects.all().order_by("-id")

    return render(
        request,
        "members/list.html",
        {
            "members": members,
            "form": form,
        },
    )


@login_required
def view_member(request, id):

    member = get_object_or_404(Member, id=id)

    payments = Payment.objects.filter(
        member=member
    ).order_by("-payment_date")

    attendance = Attendance.objects.filter(
        member=member
    ).order_by("-attendance_date")

    return render(
        request,
        "members/view.html",
        {
            "member": member,
            "payments": payments,
            "attendance": attendance,
        },
    )


@login_required
def edit_member(request, id):

    member = get_object_or_404(Member, id=id)

    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)

        if form.is_valid():
            form.save()
            return redirect("members")

    else:
        form = MemberForm(instance=member)

    return render(
        request,
        "members/edit.html",
        {
            "form": form,
            "member": member,
        },
    )


@login_required
def delete_member(request, id):

    member = get_object_or_404(Member, id=id)

    member.delete()

    return redirect("members")