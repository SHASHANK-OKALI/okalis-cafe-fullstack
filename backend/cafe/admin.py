from django.contrib import admin
from .models import MenuItem, Reservation, ContactMessage, Order, OrderItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "popular", "is_available")
    list_filter = ("category", "popular", "is_available")
    search_fields = ("name", "category")
    list_editable = ("price", "popular", "is_available")

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "time", "guests", "phone", "status", "created_at")
    list_filter = ("status", "date", "guests")
    search_fields = ("name", "email", "phone")
    list_editable = ("status",)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("subject", "name", "email", "is_read", "created_at")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "subject", "message")
    list_editable = ("is_read",)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("item_name", "unit_price", "quantity", "line_total")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_name", "phone", "fulfillment", "total", "status", "created_at")
    list_filter = ("status", "fulfillment", "created_at")
    search_fields = ("customer_name", "phone", "email")
    list_editable = ("status",)
    inlines = (OrderItemInline,)
