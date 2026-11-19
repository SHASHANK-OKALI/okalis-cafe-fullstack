from django.contrib import admin
from django.urls import path
from cafe.views import menu_list, create_reservation, create_contact_message, create_order, health


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/health/", health),
    path("api/menu/", menu_list),
    path("api/reservations/", create_reservation),
    path("api/contact/", create_contact_message),
    path("api/orders/", create_order),
]
