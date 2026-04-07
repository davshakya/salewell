from decimal import Decimal

from .catalog import get_product


CART_SESSION_KEY = "salewell_cart"
FREE_SHIPPING_THRESHOLD = Decimal("12000.00")
STANDARD_SHIPPING_FEE = Decimal("350.00")


def get_cart(request):
    return request.session.get(CART_SESSION_KEY, {})


def save_cart(request, cart):
    request.session[CART_SESSION_KEY] = cart
    request.session.modified = True


def add_item(request, slug, quantity):
    cart = get_cart(request)
    current = int(cart.get(slug, 0))
    cart[slug] = current + int(quantity)
    save_cart(request, cart)


def set_item_quantity(request, slug, quantity):
    cart = get_cart(request)
    quantity = int(quantity)
    if quantity <= 0:
        cart.pop(slug, None)
    else:
        cart[slug] = quantity
    save_cart(request, cart)


def remove_item(request, slug):
    cart = get_cart(request)
    cart.pop(slug, None)
    save_cart(request, cart)


def clear_cart(request):
    request.session.pop(CART_SESSION_KEY, None)
    request.session.modified = True


def cart_summary(request):
    raw_cart = get_cart(request)
    items = []
    subtotal = Decimal("0.00")
    item_count = 0
    sanitized_cart = {}

    for slug, raw_quantity in raw_cart.items():
        product = get_product(slug)
        quantity = int(raw_quantity)
        if product is None or quantity <= 0:
            continue

        line_total = product["price"] * quantity
        sanitized_cart[slug] = quantity
        items.append(
            {
                "product": product,
                "quantity": quantity,
                "line_total": line_total,
            }
        )
        subtotal += line_total
        item_count += quantity

    if sanitized_cart != raw_cart:
        save_cart(request, sanitized_cart)

    shipping_fee = Decimal("0.00")
    if subtotal and subtotal < FREE_SHIPPING_THRESHOLD:
        shipping_fee = STANDARD_SHIPPING_FEE

    return {
        "items": items,
        "item_count": item_count,
        "subtotal": subtotal,
        "shipping_fee": shipping_fee,
        "free_shipping_threshold": FREE_SHIPPING_THRESHOLD,
        "total": subtotal + shipping_fee,
    }
