
from django import template

register = template.Library()

@register.filter
def comma_to_br(value):
    """
    Replace commas with commas followed by <br /> tags.
    """
    return value.replace(',', ',<br />')


@register.filter
def multiply(value, arg):
    try:
        return value * arg
    except (ValueError, TypeError):
        return ''