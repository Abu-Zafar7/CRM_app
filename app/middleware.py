# middleware.py

from .views import check_due_payments

class DuePaymentsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        check_due_payments(request)  # Check for due payments and send notifications
        response = self.get_response(request)
        return response
