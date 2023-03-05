from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm


# Create your views here.
def all_products(request):
    """ A view to show all products """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """ A view to show individual products """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, "products/product_detail.html", context)


def add_product(request):
    """ Add a product to store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')  # noqa
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
