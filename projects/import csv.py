import csv

count = {"": 8, ".csv": 2, ".md": 2, ".png": 11}

with open("filecounts.csv", "a") as csvfile:
    countwriter = csv.writer(csvfile)
    data = [count[""], count[".csv"],count[".md"],count[".png"]]
    countwriter.writerow(data)

