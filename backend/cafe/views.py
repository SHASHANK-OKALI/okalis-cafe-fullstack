from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem, Reservation, ContactMessage, Order, OrderItem
from .serializers import MenuItemSerializer, ReservationSerializer, ContactMessageSerializer, OrderSerializer


@api_view(["GET"])
def health(request):
    return Response({"status": "ok", "service": "Okali's Cafe API"})

@api_view(["GET"])
def menu_list(request):
    items = MenuItem.objects.filter(is_available=True)
    category = request.query_params.get("category")
    if category and category.lower() != "all": items = items.filter(category__iexact=category)
    return Response(MenuItemSerializer(items, many=True).data)


@api_view(["POST"])
def create_reservation(request):
    serializer = ReservationSerializer(data=request.data)
    if serializer.is_valid():
        reservation = serializer.save()
        return Response({"message": "Reservation request received.", "reservation": ReservationSerializer(reservation).data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def create_contact_message(request):
    serializer = ContactMessageSerializer(data=request.data)
    if serializer.is_valid():
        message = serializer.save()
        return Response({"message": "Your message was saved successfully.", "message_id": message.id}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def create_order(request):
    data = request.data
    name = str(data.get("customer_name", "")).strip()
    phone = "".join(str(data.get("phone", "")).split())
    email = str(data.get("email", "")).strip()
    fulfillment = data.get("fulfillment", "delivery")
    address = str(data.get("delivery_address", "")).strip()
    notes = str(data.get("notes", "")).strip()
    raw_items = data.get("items", [])
    errors = {}
    if len(name) < 3: errors["customer_name"] = "Enter your name (at least 3 characters)."
    if len(phone) != 10 or not phone.isdigit() or phone[0] not in "6789": errors["phone"] = "Enter a valid 10-digit Indian mobile number."
    if fulfillment not in ["delivery", "pickup"]: errors["fulfillment"] = "Select delivery or pickup."
    if fulfillment == "delivery" and len(address) < 8: errors["delivery_address"] = "Enter a delivery address of at least 8 characters."
    if not isinstance(raw_items, list) or not raw_items: errors["items"] = "Cart must contain at least one item."
    if errors: return Response(errors, status=status.HTTP_400_BAD_REQUEST)
    try:
        with transaction.atomic():
            validated = []
            subtotal = 0
            for entry in raw_items:
                menu_id = int(entry.get("menu_item_id", entry.get("id", 0)))
                quantity = int(entry.get("quantity", 0))
                if quantity < 1 or quantity > 50: raise ValueError("Each item quantity must be between 1 and 50.")
                item = MenuItem.objects.get(pk=menu_id, is_available=True)
                line_total = item.price * quantity
                subtotal += line_total
                validated.append((item, quantity, line_total))
            delivery_charge = 40 if fulfillment == "delivery" else 0
            order = Order.objects.create(customer_name=name, phone=phone, email=email, fulfillment=fulfillment,
                delivery_address=address if fulfillment == "delivery" else "", notes=notes,
                subtotal=subtotal, delivery_charge=delivery_charge, total=subtotal + delivery_charge)
            for item, quantity, line_total in validated:
                OrderItem.objects.create(order=order, menu_item=item, item_name=item.name, unit_price=item.price, quantity=quantity, line_total=line_total)
    except MenuItem.DoesNotExist:
        return Response({"items": "One or more selected menu items are unavailable. Refresh the menu and try again."}, status=status.HTTP_400_BAD_REQUEST)
    except (ValueError, TypeError) as exc:
        return Response({"items": str(exc) or "Invalid cart item."}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"message": "Order received!", "order": OrderSerializer(order).data}, status=status.HTTP_201_CREATED)
