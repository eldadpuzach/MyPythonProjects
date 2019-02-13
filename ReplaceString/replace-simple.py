#takes 'input path'#  from the user & create 'Out' dir
#replaces chracters on all files
#puts the files after replace into the 'Out' dir
import os
import shutil

inputpath = input('Enter UNC path to files: ')
texttofind = input('1st char to find: ')
texttofind2 = input('2nd char to find: ')
texttoreplace = input('Text to replace: ')


sourcepath = os.path.normpath(inputpath)
outpath = sourcepath + 'Out/'
#Checks if Out folder is exeist
if os.path.exists(outpath):
    shutil.rmtree(outpath)
#Creates Out folder
os.mkdir(outpath, 0o777)
print("Output folder is created:", outpath)

filelist = os.listdir(sourcepath)
for file in filelist:
    inputfile = sourcepath + '/' + file
    print('Conversion is going on for: ' + inputfile)
    with open(inputfile, 'r') as inputfile:
        filedata = inputfile.read()

        freq = 0
        freq2 = 0
        freq = filedata.count(texttofind)
        outpath = outpath + '/' + file
        filedata = filedata.replace("'", "\n")
        filedata = filedata.replace(texttofind, texttoreplace)

        if texttofind2 != '':
            freq2 = filedata.count(texttofind2)
            filedata = filedata.replace(texttofind2, texttoreplace)

        with open(outpath, 'w') as file:
            file.write(filedata)
            print('1st char: total %d replaced' % freq)
            print('2nd char: total %d replaced' % freq2)
