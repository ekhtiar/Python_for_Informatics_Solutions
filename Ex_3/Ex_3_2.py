#!/usr/bin/env python
#adjust your shebang line

#Rewrite your pay program using try and except so that your program
#handles non-numeric input gracefully by printing a message and exiting the
#program. The following shows two executions of the program

#take input from user and convert to float
hours = raw_input("How many hours have you worked this week? ")

#convert to float
try:
    hours = float(hours)
except:
    print "Error, please enter numeric input"
    exit()

#take input from user and convert to float
rate = raw_input("How much is your hourly pay? ")

#convert to float
try:
    rate = float(rate)
except:
    print "Error, please enter numeric input"
    exit()

#calculate pay
if hours > 40:
    pay = rate * 40 + rate * 1.5 * (hours - 40)
else:
    pay = rate * hours

#print result
print pay