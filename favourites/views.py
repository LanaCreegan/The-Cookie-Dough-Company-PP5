from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from profiles.models import UserProfile
from products.models import Product
from .models import Favourites


def favourites(request):
    
   
    user = get_object_or_404(UserProfile, user=request.user)
    favourites = Favourites.objects.filter(user_profile=user)

    template = "favourites/favourites.html"
    context = {
        "favourites": favourites,
    }

    return render(request, template, context)


def add_to_favourites(request, product_id):
   
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    Favourites.objects.create(user_profile=user, product=product)
    messages.info(request, f"{product.name} has been added to your favourites!")

    return redirect(reverse("product_detail", args=[product.id]))


def remove_from_favourites(request, product_id):
  
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    Favourites.objects.filter(product=product, user_profile=user).delete()

    messages.info(
        request, f"{product.name} has been removed from your favourites!"
    )

    return redirect(reverse("product_detail", args=[product.id]))