# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

shortest = float('inf')
shortlist = []

longest = 0
longlist = []

index = -1


with open(r"C:\Users\lucas\Documents\Coding Nomads\python-201-main\03_file-input-output\words.txt","r") as myfile:
    lines = myfile.readlines()

    for word in lines:
        index += 1
        word = word.strip()

        if len(word) <= shortest:
            shortest = len(word)
            shortlist.append(word)
            
            if len(shortlist) == 1:
                continue
            if len(shortlist[-2])>len(shortlist[-1]):
                shortlist[:] = shortlist[-1]

        elif len(word) >= longest:
            longest = len(word)
            longlist.append(word)
            
            if len(longlist) == 1:
                continue
            elif len(longlist[-2])<len(longlist[-1]):
                longlist = longlist[-1:]
    
    total = len(lines)

    print(f"Shortest word is: {shortlist}")
    print(f"Longest word is: {longlist}")
    print(f"Total number of words are: {total}")


