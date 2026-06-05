from django.shortcuts import render, redirect
from .models import ContactSubmission


def home(request):
    return render(request, "home.html")


def contact_submit(request):
    if request.method == "POST":

        ContactSubmission.objects.create(
            full_name=request.POST.get("full_name"),
            company=request.POST.get("company"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            project_details=request.POST.get("project_details"),
            budget=request.POST.get("budget"),
        )

        return redirect("/")

    return redirect("/")