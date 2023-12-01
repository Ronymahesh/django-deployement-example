from django import template
register = template.Library()

# decorators
@register.filter(name='cut')
def cut(value,args):
    """this is an custom filter"""
    return value.replace(args,'')

# register.filter('cut',cut)
