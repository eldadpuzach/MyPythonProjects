#takes 'input path'#  from the user & create 'Out' dir
#replaces chracters on all files
#puts the files after replace into the 'Out' dir
import os
import shutil

texttofind = []
texttoreplace = []


inputpath = input('Please enter UNC path to files: ')
texttofind = input('Please separate by comma the characters You want to find: ')
texttoreplace = input('Please separate by comma the characters You want to replace: ')


sourcepath = os.path.normpath(inputpath)
outpath = sourcepath

outfolder = '/Out/'
#Checks if Out folder is exeist
if os.path.exists(outpath + outfolder):
    shutil.rmtree(outpath + outfolder)
#Creates Out folder
os.mkdir(outpath + outfolder, 0o777)
print("Output folder is created:", os.path.normpath(outpath + outfolder))
outfolderafterreplace = os.path.normpath(outpath + outfolder)
source = os.listdir(os.path.normpath(sourcepath))
for file in source:
    inputfile = source + file
    print('Conversion is going on for: ' + inputfile)
    with open(inputfile, 'r') as inputfile:
        filedata = inputfile.read()
        freq = 0
        freq = filedata.count(texttofind)
        outfolderafterreplace = outfolderafterreplace + file
        filedata = filedata.replace(texttofind,texttoreplace)
        with open(outfolderafterreplace, 'w') as file:
            file.write(filedata)
            print('Total %d records replaced' % freq)
