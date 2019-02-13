import os

# f1_path = input('Enter UNC path to folder #1: ')
# f2_path = input('Enter UNC path to folder #2: ')
f1_path = 'C:/Google Drive/Python/two_folder_diff_files/1'
f2_path = 'C:/Google Drive/Python/two_folder_diff_files/2'

f1 = os.listdir(f1_path)
f2 = os.listdir(f2_path)

f1_array = []
f2_array = []

for f in f1:
    f1_array.append(os.path.basename(f))

for f in f2:
    f2_array.append(os.path.basename(f))


print(f1_array)
print(f2_array)
folder1 = []
for i in f1_array:
    for j in f2_array:
        if j == i:
            folder1.append(i)




outfile = open('Folder1.txt', 'w')
outfile.write("\n".join(f1_array))
outfile2 = open('Folder2.txt', 'w')
outfile2.write("\n".join(f2_array))

print(folder1)




