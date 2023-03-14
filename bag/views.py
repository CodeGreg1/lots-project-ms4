from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib.staticfiles import storage
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ A view to return the shopping bag page """
    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):
    """ Adding a quantity of the specified product to the bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to x{bag[item_id]}')  # noqa
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product in the bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f'Updated quantity of {product.name} in your bag')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the specified product from the bag """

    product = Product.objects.get(pk=item_id)
    bag = request.session.get('bag', {})

    bag.pop(item_id)
    messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
