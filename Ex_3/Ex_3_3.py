#!/usr/bin/env python
#adjust your shebang line

#Write a program to prompt for a score between 0.0 and 1.0. If the
#score is out of range, print an error message. If the score is between 0.0 and 1.0,
#print a grade using the following table:
#take user input
score = raw_input("Enter score: ")

#try to convert to float
try:
    score = float(score)
except:
    print "Bad score"
    exit()

#check for valid range
if score > 1.0 or score < 0:
    print "Bad score"
    exit()

#print appropriate score
if score >= 0.9:
    print "A"
elif score >= 0.8:
    print "B"
elif score >= 0.7:
    print "C"
elif score >= 0.6:
    print "D"
elif score < 0.6:
    print "F"