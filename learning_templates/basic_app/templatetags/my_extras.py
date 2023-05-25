from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, args):
    """
    This cuts out all values of 'args' from the string
    :param value:
    :param args:
    :return:
    """
    return value.replace(args, '')

# register.filter('cut', cut)
