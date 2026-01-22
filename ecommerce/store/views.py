from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .cart import add_item, cart_items, cart_total, remove_item
from .models import Category, Product


def home(request):
    featured_products = Product.objects.filter(is_featured=True)[:6]
    categories = Category.objects.all()
    return render(
        request,
        "store/home.html",
        {
            "featured_products": featured_products,
            "categories": categories,
        },
    )


def product_list(request):
    category_id = request.GET.get("category")
    products = Product.objects.all()
    selected_category = None
    if category_id:
        selected_category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=selected_category)
    return render(
        request,
        "store/product_list.html",
        {
            "products": products,
            "categories": Category.objects.all(),
            "selected_category": selected_category,
        },
    )


def product_detail(request, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "store/product_detail.html", {"product": product})


def add_to_cart(request, product_id: int):
    add_item(request.session, product_id)
    return redirect(reverse("cart_detail"))


def remove_from_cart(request, product_id: int):
    remove_item(request.session, product_id)
    return redirect(reverse("cart_detail"))


def cart_detail(request):
    items = cart_items(request.session)
    total = cart_total(request.session)
    return render(request, "store/cart_detail.html", {"items": items, "total": total})


def checkout(request):
    items = cart_items(request.session)
    total = cart_total(request.session)
    return render(
        request,
        "store/checkout.html",
        {
            "items": items,
            "total": total,
        },
    )
