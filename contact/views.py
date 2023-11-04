from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm
from .models import Contact


def contact(request):
    context = {}
    form = ContactForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Your message has been sent!")

    template = "contact/contact.html"
    context["form"] = form
    return render(request, template, context)


