from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=120, unique=True)
    category = models.CharField(max_length=80, db_index=True)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    image = models.URLField(max_length=600, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=4.5)
    popular = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["category", "name"]
    def __str__(self): return self.name

class Reservation(models.Model):
    STATUS_CHOICES = [("pending", "Pending"), ("confirmed", "Confirmed"), ("cancelled", "Cancelled"), ("completed", "Completed")]
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.CharField(max_length=20)
    guests = models.PositiveSmallIntegerField(default=2)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-created_at"]
    def __str__(self): return f"{self.name} — {self.date} {self.time} ({self.status})"

class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=160)
    message = models.TextField(max_length=500)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-created_at"]
    def __str__(self): return f"{self.subject} — {self.name}"

class Order(models.Model):
    STATUS_CHOICES = [("received", "Received"), ("preparing", "Preparing"), ("ready", "Ready"), ("completed", "Completed"), ("cancelled", "Cancelled")]
    customer_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    fulfillment = models.CharField(max_length=12, choices=[("delivery", "Delivery"), ("pickup", "Pickup")], default="delivery")
    delivery_address = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    subtotal = models.PositiveIntegerField()
    delivery_charge = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="received")
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-created_at"]
    def __str__(self): return f"Order #{self.pk} — {self.customer_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    item_name = models.CharField(max_length=120)
    unit_price = models.PositiveIntegerField()
    quantity = models.PositiveSmallIntegerField()
    line_total = models.PositiveIntegerField()
    def __str__(self): return f"{self.item_name} × {self.quantity}"
