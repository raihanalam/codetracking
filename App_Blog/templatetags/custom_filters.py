from django import template

register = template.Library()

def range_filter(value):
     return value[0:250] + '...'

register.filter('range_filter',range_filter)