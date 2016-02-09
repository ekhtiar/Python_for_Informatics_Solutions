#!/usr/bin/env python
#adjust your shebang line

#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours
#take input from user and convert to float
hours = raw_input("How many hours have you worked this week? ")
rate = raw_input("How much is your hourly pay? ")
hours = float(hours)
rate = float(rate)

#calculate pay
if hours > 40:
    pay = rate * 40 + rate * 1.5 * (hours - 40)
else:
    pay = rate * hours

#print result
print pay