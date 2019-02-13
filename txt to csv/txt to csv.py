### Converting txt file to csv file.

# open and read the txt file.
text_file = open("Name_of_File.txt", "r")

# Read each line of text file and save it in lines.
lines = text_file.readlines()

# print lines
print(len(lines))
text_file.close()

# Call CSV Library
import csv

# Make a csv file.
mycsv = csv.writer(open('OutPut.csv', 'wb'))

# Write header for csv file.
mycsv.writerow(['year', 'month', 'date', 'hour', 'minute', 'second'])


# This is a function that works in this way that:
# Text file is reading each line and find where it has "2016"
# Then it is finding other parameters for that date.
# Spliting Date as year, month, day and other parameteres.
n = 0
for line in lines:
    n = n + 1
n = 0
for line in lines:
    n = n + 1
    if "2016" in line:
        if "[" in line:
            date_time = line.split("[")[0]
            year = date_time.split(" ")[0]
            month = date_time.split(" ")[1]
            day = date_time.split("  ")[1]
            time = date_time.split("  ")[2]
            hour = time.split(":")[0]
            minute = time.split(":")[1]
            second = time.split(":")[2]

# At the end we save all information for that specific date and then going for other date.
        mycsv.writerow([year, month, day, hour, minute, second])

