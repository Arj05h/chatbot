from .cart import cart_items, cart_total


def cart_summary(request):
    return {
        "cart_count": sum(item["quantity"] for item in cart_items(request.session)),
        "cart_total": cart_total(request.session),
    }
