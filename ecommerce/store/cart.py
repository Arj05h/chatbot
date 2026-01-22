from decimal import Decimal

from .models import Product

CART_SESSION_KEY = "cart"


def get_cart(session: dict) -> dict:
    cart = session.get(CART_SESSION_KEY, {})
    if not isinstance(cart, dict):
        cart = {}
    return cart


def save_cart(session: dict, cart: dict) -> None:
    session[CART_SESSION_KEY] = cart
    session.modified = True


def add_item(session: dict, product_id: int, quantity: int = 1) -> None:
    cart = get_cart(session)
    item = cart.get(str(product_id), {"quantity": 0})
    item["quantity"] += quantity
    cart[str(product_id)] = item
    save_cart(session, cart)


def remove_item(session: dict, product_id: int) -> None:
    cart = get_cart(session)
    cart.pop(str(product_id), None)
    save_cart(session, cart)


def cart_items(session: dict) -> list[dict]:
    cart = get_cart(session)
    product_ids = [int(pid) for pid in cart.keys()]
    products = Product.objects.filter(id__in=product_ids)
    items = []
    for product in products:
        quantity = cart.get(str(product.id), {}).get("quantity", 0)
        line_total = product.price * Decimal(quantity)
        items.append({
            "product": product,
            "quantity": quantity,
            "line_total": line_total,
        })
    return items


def cart_total(session: dict) -> Decimal:
    total = Decimal("0.00")
    for item in cart_items(session):
        total += item["line_total"]
    return total
