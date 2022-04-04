from django import template

register = template.Library()


@register.filter(name='add_comma')
def add_comma(price: int or str):
    str_price = ''
    if isinstance(price, int):
        pass
    elif isinstance(price, str):
        i = 0
        for item in price:
            if i % 3 == 0:
                str_price += ','
            str_price += item
    pass
