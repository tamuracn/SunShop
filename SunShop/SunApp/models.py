from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
Everytime you make changes to the models.py file, you need to run the following commands into terminal:
python manage.py makemigrations
python manage.py migrate

"""
class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

# class Project(models.Model):
#     name = models.CharField(max_length=100)
#     budget = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField(blank=True)

#     def __str__(self):
#         return self.name

class PurchaseRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('ordered', 'Ordered'),
        ('received', 'Received'),
    ]

    item_name = models.CharField(max_length=200)
    purchase_link = models.URLField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    ordered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='ordered_by')
    received_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='received_by')
    packing_slip = models.FileField(upload_to='packing_slips/', blank=True, null=True)

    def __str__(self):
        return self.item_name