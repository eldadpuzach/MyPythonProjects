import re
import os

#list all files in current work dir
list_folder = os.listdir(os.getcwd())

#create output.csv file & write a header for it
header = ['Document#', ',', 'Date', '\n']
outfile = open('output.csv', 'w')
outfile.write("".join(header))

#iterates over each file in current dir
for f in list_folder:
    base_file, ext = os.path.splitext(f)
    if ext != ".py":
        if ext != ".csv":
            if ext != ".ini":
                lines = []  # Declare an empty list named "lines"
                array = []

                with open(f, 'r') as in_file:  # Opens each file in for loop for reading of text data.
                    for line in in_file:  # For each line of text in in_file
                        BGM = re.search("351\+(.+?)\+009", line).group(1)
                        DTM = re.search("137:(.+?):", line).group(1)
                        array.extend([BGM, ',', DTM, "\n"])

                        outfile = open('output.csv', 'a')
                        outfile.write("".join(array))
