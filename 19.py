'''

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

'''

import datetime


def p19():
    days_of_mont = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0 #Monday
    sundays = 0
    year = 1900
    days = sum(days_of_mont)
    if year % 4 == 0:
        days += 1
    for x in range(0, days):#setting starting day
        day += 1
        if day == 7:
            day = 0
    for year in range(1901, 2001):
        if year % 4 == 0:
            days_of_mont[1] = 29
        else:
            days_of_mont[1] = 28
        for days in days_of_mont:
            for x in range(0, days):
                day += 1
                if x == 0:
                    if day == 7:
                        sundays += 1
                if day == 7:
                    day = 0
    return sundays

tt1 = datetime.datetime.now()

print('Answer: ', p19())

tt2 = datetime.datetime.now()

print('Time: ', tt2 - tt1) #0.003 seconds