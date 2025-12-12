from decimal import Decimal

from django.db import models
from django.contrib.auth.models import User


class LaundryOrder(models.Model):
    SERVICE_CHOICES = [
        ('reguler', 'Reguler (2–3 hari)'),
        ('express', 'Express (1 hari)'),
        ('kilat', 'Kilat (6 jam)'),
    ]

    STATUS_CHOICES = [
        ('request', 'Permintaan Masuk'),
        ('pickup', 'Dijemput Driver'),
        ('washing', 'Sedang Dicuci'),
        ('delivering', 'Sedang Diantar'),
        ('done', 'Selesai'),
    ]

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='laundry_orders'
    )
    address = models.CharField(max_length=255)
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    pickup_time = models.CharField(max_length=100, blank=True)

    # FITUR BARU
    weight_kg = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )
    note = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='request'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def price_per_kg(self) -> Decimal:
        """Tarif per kg berdasarkan jenis layanan."""
        if self.service_type == 'express':
            return Decimal('9000')
        if self.service_type == 'kilat':
            return Decimal('11000')
        return Decimal('7000')  # reguler

    @property
    def total_price(self) -> Decimal:
        """Estimasi harga = berat * tarif per kg."""
        if not self.weight_kg:
            return Decimal('0')
        return self.weight_kg * self.price_per_kg

    def __str__(self):
        return f"Order #{self.id} - {self.customer.username}"
