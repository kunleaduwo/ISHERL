import requests
from django.conf import settings

PAYSTACK_SECRET_KEY = settings.PAYSTACK_SECRET_KEY

def initialize_payment(email, amount, reference, callback_url):
    url = "https://api.paystack.co/transaction/initialize"
    headers = {
        "Authorization": f"Bearer {PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "email": email,
        "amount": amount * 100,  # kobo
        "reference": reference,
        "callback_url": callback_url
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()
