from urllib.parse import urlencode

from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from .cart import add_item, cart_summary, clear_cart, remove_item, set_item_quantity
from .catalog import CATEGORY_DETAILS, featured_products, get_product, list_products, related_products
from .forms import AddToCartForm, CheckoutForm, LeadForm, OrderLookupForm
from .models import Lead, Order, OrderItem


def build_context(request, **extra):
    summary = cart_summary(request)
    context = {
        "cart_data": summary,
        "cart_count": summary["item_count"],
        "category_details": CATEGORY_DETAILS,
    }
    context.update(extra)
    return context


def index(request):
    if request.method == "POST" and request.POST.get("form_type") == "lead":
        lead_form = LeadForm(request.POST)
        if lead_form.is_valid():
            lead_form.save()
            messages.success(
                request,
                "Your request has been received. SaleWell IoT will follow up with the right water tank setup and installation guidance.",
            )
            return HttpResponseRedirect(f"{reverse('index')}#catalogue-request")
    else:
        lead_form = LeadForm(initial={"interest": Lead.HOME})

    return render(
        request,
        "index.html",
        build_context(
            request,
            page_title="SaleWell IoT | Smart Water Tank Automation",
            lead_form=lead_form,
            featured_products=featured_products(),
            residential_products=list_products("residential")[:3],
            commercial_products=list_products("commercial")[:3],
        ),
    )


def category_page(request, category):
    category_meta = CATEGORY_DETAILS.get(category)
    if category_meta is None:
        raise Http404("Unknown category")

    return render(
        request,
        "category.html",
        build_context(
            request,
            page_title=f"SaleWell IoT | {category_meta['title']}",
            current_category=category,
            category_meta=category_meta,
            products=list_products(category),
        ),
    )


def product_detail(request, slug):
    product = get_product(slug)
    if product is None:
        raise Http404("Product not found")

    return render(
        request,
        "product_detail.html",
        build_context(
            request,
            page_title=f"SaleWell IoT | {product['name']}",
            product=product,
            add_to_cart_form=AddToCartForm(),
            related_products=related_products(product),
        ),
    )


@require_POST
def add_to_cart_view(request, slug):
    product = get_product(slug)
    if product is None:
        raise Http404("Product not found")

    form = AddToCartForm(request.POST)
    quantity = 1
    if form.is_valid():
        quantity = form.cleaned_data["quantity"]

    add_item(request, slug, quantity)
    messages.success(request, f"{product['name']} added to your cart.")
    return redirect(request.POST.get("next") or reverse("cart"))


def cart_view(request):
    if request.method == "POST":
        for item in cart_summary(request)["items"]:
            slug = item["product"]["slug"]
            quantity = request.POST.get(f"qty_{slug}", item["quantity"])
            try:
                set_item_quantity(request, slug, int(quantity))
            except (TypeError, ValueError):
                continue
        messages.success(request, "Your cart has been updated.")
        return redirect("cart")

    return render(
        request,
        "cart.html",
        build_context(
            request,
            page_title="SaleWell IoT | Your Cart",
        ),
    )


@require_POST
def remove_from_cart_view(request, slug):
    product = get_product(slug)
    remove_item(request, slug)
    if product:
        messages.info(request, f"{product['name']} removed from your cart.")
    return redirect("cart")


def checkout(request):
    summary = cart_summary(request)
    if not summary["items"]:
        messages.info(request, "Your cart is empty. Add a smart water tank solution before checkout.")
        return redirect("index")

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.subtotal = summary["subtotal"]
            order.shipping_fee = summary["shipping_fee"]
            order.total_amount = summary["total"]
            order.save()

            OrderItem.objects.bulk_create(
                [
                    OrderItem(
                        order=order,
                        product_slug=item["product"]["slug"],
                        product_name=item["product"]["name"],
                        category=item["product"]["category"],
                        product_type=item["product"]["product_type"],
                        unit_price=item["product"]["price"],
                        quantity=item["quantity"],
                        line_total=item["line_total"],
                    )
                    for item in summary["items"]
                ]
            )
            clear_cart(request)
            messages.success(request, f"Order {order.order_number} has been placed successfully.")
            query = urlencode(
                {
                    "order_number": order.order_number,
                    "email": order.email,
                    "placed": "1",
                }
            )
            return redirect(f"{reverse('orders')}?{query}")
    else:
        form = CheckoutForm(initial={"delivery_area": "India"})

    return render(
        request,
        "checkout.html",
        build_context(
            request,
            page_title="SaleWell IoT | Checkout",
            checkout_form=form,
        ),
    )


def orders_view(request):
    orders = []
    lookup_form = OrderLookupForm(request.GET or None)
    show_results = False

    if request.GET:
        show_results = True
        if lookup_form.is_valid():
            orders_query = Order.objects.prefetch_related("items").all()
            email = lookup_form.cleaned_data.get("email")
            order_number = lookup_form.cleaned_data.get("order_number")
            if email:
                orders_query = orders_query.filter(email__iexact=email)
            if order_number:
                orders_query = orders_query.filter(order_number__iexact=order_number)
            orders = list(orders_query[:10])

    return render(
        request,
        "orders.html",
        build_context(
            request,
            page_title="SaleWell IoT | Orders",
            order_lookup_form=lookup_form,
            orders=orders,
            show_results=show_results,
            order_placed=request.GET.get("placed") == "1",
        ),
    )
