
"""
docstring :
this program is meant to calculate an employees weekly wage.

#input
the hourly wage
total regular hours 
total overtime hours 

#output
total weekly pay.
ot = 1.5 the hourly wage 
"""

hourlyWage = float(input("enter your hourly wage: "))
regularHours = float(input("enter your regular hours of work this week: "))
overTimeHours = float(input("enter your overtime hours of work this week: "))

regularWage = hourlyWage*regularHours
overtimeWage = (hourlyWage*1.5)*overTimeHours
totalWeeklyPay = regularWage+overtimeWage

print("your total pay this week is: ", "%.2f" % totalWeeklyPay, " pounds.")

""" Test Cases :
1.worked with all int input
2.worked with weird sf wage but looks unpresentable
3.worked with realistic wage and hours but looks unpresentable so tried to round up using formatting, worked
4.entered 11.5 as hours input to account for breaks not covered, error invalid literal for int(), changed to float

"""