from django import template

register = template.Library()


@register.filter
def custom_range(number):
    return range(int(number))
