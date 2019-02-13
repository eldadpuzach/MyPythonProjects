import re
import os
# import configparser
# import codecs

config = configparser.ConfigParser()
config.read(os.getcwd() + "/config.ini")

searchBGMvaluefrom = config['BGMfind']['fromcharacter']
searchBGMvalueto = config['BGMfind']['tocharacter']

searchDTMfrom = config['DTMfind']['fromcharacter']
searchDTMto = config['DTMfind']['tocharacter']

# replaceCharacter = codecs.decode(replaceCharacter, "unicode-escape")

#list all files in current work dir
list_folder = os.listdir(os.getcwd())

#create output.csv file & write a header for it
header = ['Document#', ',', 'Date', '\n']
outfile = open('output.csv', 'w')
outfile.write("".join(header))

my_regex = r"351\+(.+?)\+009"

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
                        BGM = re.search(my_regex, line).group(1)
                        DTM = re.search("137:(.+?):", line).group(1)
                        array.extend([BGM, ',', DTM, "\n"])

                        outfile = open('output.csv', 'a')
                        outfile.write("".join(array))
