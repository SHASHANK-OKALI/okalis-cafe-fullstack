from datetime import date
from rest_framework import serializers
from .models import MenuItem, Reservation, ContactMessage, Order, OrderItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ["id", "name", "category", "description", "price", "image", "rating", "popular", "is_available"]

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["id", "name", "email", "phone", "date", "time", "guests", "message", "status", "created_at"]
        read_only_fields = ["id", "status", "created_at"]
    def validate_name(self, value):
        value = value.strip()
        if len(value) < 3: raise serializers.ValidationError("Name must be at least 3 characters.")
        return value
    def validate_phone(self, value):
        value = "".join(value.split())
        if not value.isdigit() or len(value) != 10 or value[0] not in "6789": raise serializers.ValidationError("Enter a valid 10-digit Indian mobile number.")
        return value
    def validate_date(self, value):
        if value < date.today(): raise serializers.ValidationError("Reservation date cannot be in the past.")
        return value
    def validate_guests(self, value):
        if not 1 <= value <= 10: raise serializers.ValidationError("Guest count must be between 1 and 10.")
        return value

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ["id", "name", "email", "subject", "message", "is_read", "created_at"]
        read_only_fields = ["id", "is_read", "created_at"]
    def validate_name(self, value):
        value = value.strip()
        if len(value) < 3: raise serializers.ValidationError("Name must be at least 3 characters.")
        return value
    def validate_subject(self, value):
        value = value.strip()
        if len(value) < 3: raise serializers.ValidationError("Subject must be at least 3 characters.")
        return value
    def validate_message(self, value):
        value = value.strip()
        if len(value) < 10: raise serializers.ValidationError("Message must be at least 10 characters.")
        return value

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["item_name", "unit_price", "quantity", "line_total"]

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ["id", "customer_name", "phone", "email", "fulfillment", "delivery_address", "notes", "subtotal", "delivery_charge", "total", "status", "created_at", "items"]
        read_only_fields = fields
