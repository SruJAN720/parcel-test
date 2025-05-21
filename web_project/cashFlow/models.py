from django.db import models
from django.utils import timezone

class Transaction(models.Model):
    order_id = models.CharField(max_length=100, default="ORDER0000")  # Default placeholder order ID
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # Default amount
    currency = models.CharField(max_length=3, choices=[("INR", "INR"), ("USD", "USD")], default="INR")
    payment_method = models.CharField(
        max_length=50,
        choices=[
            ("Cash", "Cash"),
            ("Bank Transfer", "Bank Transfer"),
            ("Credit Card", "Credit Card"),
            ("PayPal", "PayPal"),
        ],
        default="Cash"
    )
    payer_name = models.CharField(max_length=100, default="Unknown")
    reference_number = models.CharField(max_length=100, blank=True, null=True)
    payment_date = models.DateField(default=timezone.now)
    status = models.CharField(
        max_length=20,
        choices=[
            ("Pending", "Pending"),
            ("Completed", "Completed"),
            ("Failed", "Failed"),
        ],
        default="Pending"
    )
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.order_id} - {self.payer_name}"
