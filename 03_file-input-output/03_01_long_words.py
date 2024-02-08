# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).
from pathlib import Path

my_path = Path(r"C:\Users\lucas\Documents\Coding Nomads\python-201-main\03_file-input-output\words.txt")
words = []

with open(my_path,'r') as myfile:
    for word in myfile.readlines():
        if len(word)>20:
            word = word.rstrip()
            words.append(word)

print(words)
