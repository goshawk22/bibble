'''
Converts a text file created by english_words_sort into a ts file to be appended to validGuess.ts
'''

# Length of word to use
word_length = 7
path = 'bibble_files/english/english_words_' + str(word_length) + '.txt'
with open(path, 'r') as handle:
    words = handle.readlines()

print(len(words))

### valid guesses ###
with open('src/constants/validGuesses.ts', 'r') as handle:
    valid = handle.readlines()

length = len(valid) 

new_valid = []
new_valid.append(valid[0])

for word in words:
    string = "  '" + word[:-1] + "',\n"
    new_valid.append(string)

new_valid.append(']')

with open('src/constants/validGuesses.ts', 'w') as handle:
    handle.writelines(new_valid)