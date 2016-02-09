"""date manipulation tools"""

from dateutil.parser import parse as dparse
from dateutil.relativedelta import relativedelta
import datetime


def parse_date(date):
    if not isinstance(date, datetime.date):
        date = str(date)
        return dparse(date)
    else:
        return date
