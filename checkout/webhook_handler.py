from django.http import HttpResponse


class stripeWH_Handler:
    """ 
    Handle Stripe webhooks 
    """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ 
        Handle a generic/unexpected/unknown webhook event
        """
        return HttpResponse(
            content=f'webhook received: {event["type"]}',
            status=200)

