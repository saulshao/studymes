from django import template
from factory.models import *
register  = template.Library()

@register.inclusion_tag("includes/region_tree_part.html")
def region_tree(region):
    return {'subregions':region.children.all()}