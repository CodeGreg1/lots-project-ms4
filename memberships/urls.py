from django.urls import path
from .views import gocardless_webhook

urlpatterns = [
    path('webhooks/gocardless/', gocardless_webhook, name='gocardless_webhook'),
    # ...other URL patterns...
]