#!/usr/bin/env python
#adjust your shebang line

#Excercise 2.3: Write a program to prompt the user for hours and rate per hour to compute gross pay
#Inform the user about the functionality of the program
print("This program calculates your gross pay")
#take input and store in appropriate variables
hours = raw_input("Please enter hours you have worked:\n")
rate = raw_input("Please enter your hourly rate:\n")
#calculate total pay and print output
total = float(hours) * float (rate)
print('Your gross pay is: ')
print(total);

