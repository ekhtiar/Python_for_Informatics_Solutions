#!/usr/bin/env python
#adjust your shebang line

#Excercise 2.5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature
#Inform the user about the functionality of the program
print("This program converts Celsius temperature Fahrenheit")
#take user input
temp_celc = raw_input("Please enter the temperature in Celsius:\n")
#Convert and print
temp_fahr = float(temp_celc)*1.8 + 32
print("In Fahrenheit it is: ")
print(temp_fahr)


