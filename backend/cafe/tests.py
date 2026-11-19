from rest_framework.test import APITestCase
from rest_framework import status
from .models import MenuItem, Reservation, ContactMessage, Order

class PublicApiTests(APITestCase):
    def test_health_endpoint(self):
        response = self.client.get('/api/health/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'ok')

    def test_contact_message_is_saved(self):
        response = self.client.post('/api/contact/', {
            'name': 'Test Customer', 'email': 'test@example.com',
            'subject': 'Test cafe message', 'message': 'This is a test message for the cafe.'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ContactMessage.objects.count(), 1)

    def test_reservation_is_saved(self):
        response = self.client.post('/api/reservations/', {
            'name': 'Test Customer', 'email': 'test@example.com', 'phone': '9876543210',
            'date': '2030-12-30', 'time': '07:00 PM', 'guests': 2, 'message': 'Window seat if possible.'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reservation.objects.count(), 1)

    def test_order_uses_server_menu_price(self):
        item = MenuItem.objects.create(name='Test Coffee', category='Coffee', price=100, is_available=True)
        response = self.client.post('/api/orders/', {
            'customer_name': 'Test Customer', 'phone': '9876543210', 'fulfillment': 'pickup',
            'items': [{'menu_item_id': item.id, 'quantity': 2}]
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        order = Order.objects.get()
        self.assertEqual(order.subtotal, 200)
        self.assertEqual(order.delivery_charge, 0)
        self.assertEqual(order.total, 200)
