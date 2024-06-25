
# Create your views here.
from django.shortcuts import get_object_or_404, render
from .models import Order


def generate_invoice(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    total_price = 0

    # Calculate total price for the order
    for item in order.invoiceitem_set.all():
        total_price += item.price_product_size.price * item.quantity

    # Initialize final_price
    final_price = total_price

    # Apply discount if it exists
    if order.discount:
        final_price = total_price * ((100 - order.discount) / 100)

    context = {
        'order': order,
        'total_price': total_price,
        'final_price': final_price,
    }
    return render(request, 'get-invoice.html', context)