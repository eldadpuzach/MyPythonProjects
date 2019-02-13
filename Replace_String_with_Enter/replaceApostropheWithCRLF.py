import os
import configparser
import codecs

list_folder = os.listdir(os.getcwd())

config = configparser.ConfigParser()
config.read(os.getcwd() + "/config.ini")

searchCharacter = config['find']['character']
replaceCharacter = config['replace']['character']
replaceCharacter = codecs.decode(replaceCharacter, "unicode-escape")

for f in list_folder:
    base_file, ext = os.path.splitext(f)
    if ext != ".py":
        if ext != ".exe":
            if ext != ".ini":
                with open(f, "r") as inputfile:
                    newText = inputfile.read().replace(searchCharacter, replaceCharacter)

                with open(f, "w") as outputfile:
                    outputfile.write(newText)
                os.rename(f, f + '.txt')

