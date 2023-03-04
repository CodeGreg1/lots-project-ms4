from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
import json


@csrf_exempt
def gocardless_webhook(request):
    if request.method != 'POST':
        return HttpResponseBadRequest('Invalid request method')

    data = json.loads(request.body)
    # do something with the webhook data here, such as updating your database 
    # or sending an email
    return HttpResponse('Webhook received')


@csrf_exempt
def gocardless_webhook(request):
    if request.method == 'POST':
        # Parse the JSON payload from the webhook
        payload = json.loads(request.body.decode('utf-8'))
        # Extract the relevant data from the payload
        event_type = payload['events'][0]['event_type']
        payment_id = payload['events'][0]['links']['payment']
        # Process the data as needed (e.g. update a database record)
        # ...
        # Return a success response
        return HttpResponse(status=200)
    else:
        # Return an error response if the request method is not POST
        return HttpResponse(status=405)


@csrf_exempt
def process_webhook(request):
    # Check that the request came from GoCardless
    if request.META.get('HTTP_WEBHOOK_SIGNATURE') != calculate_signature(request.body):
        return HttpResponse(status=403)

    # Parse the webhook payload
    payload = json.loads(request.body)

    # Check the event type and take appropriate action
    if payload['event_type'] == 'payment_created':
        # Handle payment created event
        pass
    elif payload['event_type'] == 'payment_failed':
        # Handle payment failed event
        pass
    else:
        # Ignore unknown event types
        pass

    return HttpResponse(status=200)


def calculate_signature(payload):
    # Replace with your actual webhook secret
    secret = 'your_webhook_secret_here'
    return hmac.new(secret.encode('utf-8'), payload, hashlib.sha256).hexdigest()
