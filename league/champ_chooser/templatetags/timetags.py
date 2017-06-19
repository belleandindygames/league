from django import template
import datetime
register = template.Library()

def epoch_to_date(timestamp):
    try:
        ts = float(timestamp/1000)
    except ValueError:
        return None
    return datetime.datetime.fromtimestamp(ts)

register.filter(epoch_to_date)