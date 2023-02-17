from decimal import Decimal


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    if total < 1000:
        delivery = total * Decimal(0.15)
    else:
        delivery = 1 * product_count

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
