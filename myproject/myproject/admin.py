from django.contrib import admin

from .models import Lead, Order, OrderItem


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "interest", "created_at")
    search_fields = ("name", "email", "message")
    list_filter = ("interest", "created_at")
    ordering = ("-created_at",)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("product_name", "product_type", "unit_price", "quantity", "line_total")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_number", "customer_name", "email", "status", "total_amount", "created_at")
    search_fields = ("order_number", "customer_name", "email", "phone")
    list_filter = ("status", "created_at", "delivery_area")
    readonly_fields = ("order_number", "subtotal", "shipping_fee", "total_amount", "created_at")
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("product_name", "order", "quantity", "line_total")
    search_fields = ("product_name", "order__order_number")
