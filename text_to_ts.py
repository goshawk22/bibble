'''
Converts a text file created by bible_unique_sort into a ts file to be appended to wordlist.ts and validGuess.ts
'''

with open('bible_words_5.txt', 'r') as handle:
    words = handle.readlines()

print(len(words))

### wordlist ###
with open('src/constants/wordlist.ts', 'r') as handle:
    wordlist = handle.readlines()

print(wordlist[1])

new_wordlist = []
new_wordlist.append(wordlist[0])

for word in words:
    string = "  '" + word[:-1] + "',\n"
    new_wordlist.append(string)

new_wordlist.append(']')

with open('src/constants/wordlist.ts', 'w') as handle:
    handle.writelines(new_wordlist)

### valid guesses ###
with open('src/constants/validGuesses.ts', 'r') as handle:
    valid = handle.readlines()

length = len(valid) 

new_valid = []
for i in range(length - 1):
    new_valid.append(valid[i])

for word in words:
    string = "  '" + word[:-1] + "',\n"
    if not string in new_valid:
        new_valid.append(string)

new_valid.append(']')

with open('src/constants/validGuesses.ts', 'w') as handle:
    handle.writelines(new_valid)