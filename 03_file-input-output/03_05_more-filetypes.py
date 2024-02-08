# Adapt your file counter script so that it records more different file types
# in your CSV file. Remember that the format of your output needs to be
# consistent across multiple runs of your script. This means you'll need to
# make a compromise and choose which file types you want to record beforehand.


import csv
from pathlib import Path

# The path to my Desktop
current_location = Path(r"C:\users\lucas\Desktop")
# The path to the csv file
myfile = Path(r"C:\Users\lucas\Documents\Coding Nomads\python-201-main\03_file-input-output\file-counter\filecounts.csv")

dict_files = {}

# Filling dictionary with the diffferent file types and how many there are of that file type.
for file in current_location.iterdir():
    if file.suffix not in dict_files.keys():
        dict_files[file.suffix] = 1
    else:
         dict_files[file.suffix] += 1
print(dict_files)
# Opening the file and appending the dictionary values.
with open(myfile, "a") as csvfile:
    countwriter = csv.writer(csvfile)
    data = []
    for file in dict_files:
        data.append(dict_files[file])
    countwriter.writerow(data)

# Reading the content of the file with the dictionary values.
with open(myfile,"r") as csvfile:
    lines = csvfile.readline()
    reader = csv.DictReader(csvfile, fieldnames=[".ini", "folder", ".lnk","xlsx"])
    counts = list(reader)

print(counts)
