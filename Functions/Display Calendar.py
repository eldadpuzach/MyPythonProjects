# Python program to display calendar of given month of the year

# import module
import calendar

yy = 2018
mm = 10

# To ask month and year from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
for i in range(1, 13):
    print(calendar.month(yy, i))