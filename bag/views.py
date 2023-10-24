from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ A view to renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the bag """


    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    filled = None
    if 'is_filled' in request.POST:
        filled = request.POST['product_is_filled']
    bag = request.session.get('bag', {})

    if filled:
        if item_id in list(bag.keys()):
            if filled in bag[item_id][''].keys():
                bag[item_id]['items_is_filled'][filled] += quantity
            else:
                bag[item_id]['items_is_filled'][filled] = quantity
        else:
            bag[item_id] = {'items_is_filled': {filled: quantity}}

    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)

def update_bag(request, item_id):
    """ Update a quantity of the specified product in the bag """

    quantity = int(request.POST.get('quantity'))
    filled = None
    if 'is_filled' in request.POST:
        size = request.POST['is_filled']
    bag = request.session.get('bag', {})

    if filled:
        if quantity > 0:
            bag[item_id]['items_is_filled'][filled] = quantity
        else:
            del bag[item_id]['items_is_filled'][filled]
            if not bag[item_id]['items_is_filled']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove product from the shopping bag """

    try:
        filled = None
        if 'product_is_filled' in request.POST:
            size = request.POST['product_is_filled']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_is_filled'][filled]
            if not bag[item_id]['items_is_filled']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)

    