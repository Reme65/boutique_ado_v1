from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    if price is None:
        return 0

    # If quantity is a dictionary, extract the numeric value safely
    if isinstance(quantity, dict):
        # Handle the inner 'items_by_size' nested format if present
        if 'items_by_size' in quantity:
            quantity = quantity['items_by_size']

        # Sum individual sizes. Example:
        # {'s': 1, 'm': 2} becomes 3
        return price * sum(int(qty) for qty in quantity.values())

    # Fallback safety: if something went wrong and it's not a number,
    # default to 1 item.
    try:
        return price * int(quantity)
    except (ValueError, TypeError):
        return price * 1
