import filecmp

# f1_path = input('Enter UNC path to folder #1: ')
# f2_path = input('Enter UNC path to folder #2: ')
f1_path = 'C:/Google Drive/Python/two_folder_diff_files/1'
f2_path = 'C:/Google Drive/Python/two_folder_diff_files/2'

dc = filecmp.dircmp(f1_path, f2_path)
dc.report()
