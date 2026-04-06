from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import LeadForm


def index(request):
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thanks. Your catalogue request has been saved and is ready for follow-up.",
            )
            return HttpResponseRedirect(f"{reverse('index')}#contact")
    else:
        form = LeadForm()

    return render(request, "index.html", {"form": form})
