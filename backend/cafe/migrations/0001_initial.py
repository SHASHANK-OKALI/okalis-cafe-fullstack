from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(name="MenuItem", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("name", models.CharField(max_length=120, unique=True)), ("category", models.CharField(db_index=True, max_length=80)),
            ("description", models.TextField(blank=True)), ("price", models.PositiveIntegerField()),
            ("image", models.URLField(blank=True, max_length=600)), ("rating", models.DecimalField(decimal_places=1, default=4.5, max_digits=2)),
            ("popular", models.BooleanField(default=False)), ("is_available", models.BooleanField(default=True)),
            ("created_at", models.DateTimeField(auto_now_add=True)), ("updated_at", models.DateTimeField(auto_now=True)),
        ], options={"ordering": ["category", "name"]}),
        migrations.CreateModel(name="Reservation", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("name", models.CharField(max_length=120)), ("email", models.EmailField(max_length=254)), ("phone", models.CharField(max_length=15)),
            ("date", models.DateField()), ("time", models.CharField(max_length=20)), ("guests", models.PositiveSmallIntegerField(default=2)),
            ("message", models.TextField(blank=True)), ("status", models.CharField(choices=[("pending", "Pending"), ("confirmed", "Confirmed"), ("cancelled", "Cancelled"), ("completed", "Completed")], default="pending", max_length=15)),
            ("created_at", models.DateTimeField(auto_now_add=True)),
        ], options={"ordering": ["-created_at"]}),
        migrations.CreateModel(name="ContactMessage", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("name", models.CharField(max_length=120)), ("email", models.EmailField(max_length=254)),
            ("subject", models.CharField(max_length=160)), ("message", models.TextField(max_length=500)),
            ("is_read", models.BooleanField(default=False)), ("created_at", models.DateTimeField(auto_now_add=True)),
        ], options={"ordering": ["-created_at"]}),
        migrations.CreateModel(name="Order", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("customer_name", models.CharField(max_length=120)), ("phone", models.CharField(max_length=15)), ("email", models.EmailField(blank=True, max_length=254)),
            ("fulfillment", models.CharField(choices=[("delivery", "Delivery"), ("pickup", "Pickup")], default="delivery", max_length=12)),
            ("delivery_address", models.TextField(blank=True)), ("notes", models.TextField(blank=True)),
            ("subtotal", models.PositiveIntegerField()), ("delivery_charge", models.PositiveIntegerField(default=0)), ("total", models.PositiveIntegerField()),
            ("status", models.CharField(choices=[("received", "Received"), ("preparing", "Preparing"), ("ready", "Ready"), ("completed", "Completed"), ("cancelled", "Cancelled")], default="received", max_length=15)),
            ("created_at", models.DateTimeField(auto_now_add=True)),
        ], options={"ordering": ["-created_at"]}),
        migrations.CreateModel(name="OrderItem", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("item_name", models.CharField(max_length=120)), ("unit_price", models.PositiveIntegerField()), ("quantity", models.PositiveSmallIntegerField()),
            ("line_total", models.PositiveIntegerField()), ("menu_item", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="cafe.menuitem")),
            ("order", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="items", to="cafe.order")),
        ]),
    ]
