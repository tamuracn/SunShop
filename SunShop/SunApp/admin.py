from django.contrib import admin
from .models import TodoItem, PurchaseRequest, PurchaseReceived, PurchaseOrder

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(PurchaseRequest)
admin.site.register(PurchaseReceived)
admin.site.register(PurchaseOrder)