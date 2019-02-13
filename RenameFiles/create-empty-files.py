import os
# change path as described by Corey,
# or leave as is and move folder
os.chdir('C:/Google Drive/Python/two_folder_diff_files/1')
listoffiles = ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt', ]

for fname in listoffiles:
    with open(fname, 'a'):
        pass
        print('Complete:', fname)
