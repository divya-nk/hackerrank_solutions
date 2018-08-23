'''
The calendar module allows you to output calendars and provides additional useful functions for them.
class calendar.TextCalendar([firstweekday])
This class can be used to generate plain text calendars.

'''

#Task - You are given a date. Your task is to find what the day is on that date.
# Input Format - A single line of input containing the space separated month, day and year, respectively, in MM DD YYY format.
# output format - Output the correct day in capital letters.

import calendar
mm, dd, yyyy = map(int, input().split(' '))
weekday = calendar.weekday(yyyy, mm, dd)
print(list(calendar.day_name)[weekday].upper())
