# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.

with open(r"C:\Users\lucas\Documents\Coding Nomads\python-201-main\03_file-input-output\words.txt","r") as file1:
    lines = file1.read()

with open(r"C:\Users\lucas\Documents\Coding Nomads\python-201-main\03_file-input-output\words_reverse.txt","w") as file2:
    file2.write(f"{lines[::-1]}")
