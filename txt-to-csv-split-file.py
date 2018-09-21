import csv
import itertools

with open('/home/eldad/Desktop/PycharmProjects/ReplaceString/InputFiles/Src.SUPDES.7290058141425.909731.1.243', 'r') as in_file:
    lines = in_file.read().splitlines()
    stripped = [line.replace(","," ").split() for line in lines]
    grouped = itertools.(*[stripped]*1)
    with open('log.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('title', 'intro', 'tagline'))
        for group in grouped:
            writer.writerows(group)