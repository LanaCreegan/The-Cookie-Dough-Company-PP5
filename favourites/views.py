from django.shortcuts import render, redirect


def favourites(request):

    return render(request, "favourites/favourites.html")
