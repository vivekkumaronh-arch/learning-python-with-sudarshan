# Different ways to import a library

import calendar
print(calendar.month(2026,12))
print(calendar.calendar(2026))
 
import calendar as c
print(c.month(2026,6))



from calendar import *
print(calendar(2026))
print(month(2026,5))



from calendar import month
print(month(2026,3))

from calendar import month as m
print(m(2026,4))



