from django import template
register = template.Library()

@register.filter
def get_value_by_index(indexable, i):
    return indexable[i]