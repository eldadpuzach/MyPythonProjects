import os

os.chdir('C:/Google Drive/Python/RenameFiles/files-to-rename')
print(os.getcwd())

for f in os.listdir():
      print(alldirfiles)
      print(os.path.splitext(f))
    f_name, f_ext = os.path.splitext(f)
print(file_name.split('-'))
    # f_title, f_course, f_num, f_songname = f_name.split('-')
    # # print(f_num)
    # f_num = f_num.strip().zfill(2)
    # f_songname = f_songname.strip()
    # f_course = f_course.strip()[:-14]
    # f_title = f_title.strip()
    #
    # # print('{}-{}{}'.format(f_num, f_songname, f_ext))
    # new_name = '{}-{}{}'.format(f_num, f_songname, f_ext)
    # os.rename(f, new_name)