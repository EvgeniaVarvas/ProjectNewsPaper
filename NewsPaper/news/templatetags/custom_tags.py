from django import template
from datetime import datetime

register = template.Library()

@register.simple_tag()
def current_time(format_string='%d.%F.%Y ') -> str: return datetime.now().strftime(format_string)  # (=)