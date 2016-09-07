import datetime
from dateutil.relativedelta import relativedelta
import sys

args = sys.argv[1:]

today = datetime.datetime.today()
target = datetime.datetime.strptime(args[0], '%m/%d/%Y')

days = target.date() - today.date()

#print "Days until {}: {}".format(args[0], days.days)
if days.days != 1:
	print "{} days".format(days.days)
else:
	print "{} day".format(days.days)
