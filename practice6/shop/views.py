from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .models import Product
from .forms import ProductForm


def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Товар успішно створено.")
            return redirect("product_list")
    else:
        form = ProductForm()

    return render(
        request,
        "shop/product_form.html",
        {
            "form": form,
            "page_title": "Створення товару",
        },
    )


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            messages.success(request, "Товар успішно оновлено.")
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)

    return render(
        request,
        "shop/product_form.html",
        {
            "form": form,
            "page_title": "Редагування товару",
        },
    )


def product_list(request):
    products = Product.objects.all()

    return render(
        request,
        "shop/product_list.html",
        {"products": products},
    )

