'''
Reads the text file created by process_json.py to get information about the length of words in the bible
Then saves the words into separate lists based on the length of the word
'''

test = "hi"
print(len(list(test)))

with open('bible_words.txt', 'r') as handle:
    bible_words = handle.readlines()

print(len(bible_words))

count = {}

for word in bible_words:
    letters = list(word)
    length = len(letters) - 1 # Don't count the \n bit

    if not length in count:
        count[length] = 1
    
    else:
        count[length] += 1

sorted_count = {}

for i in sorted(count):
   sorted_count[i] = count[i]

print(sorted_count)

for length in sorted(count):
    file_name = "bible_words_" + str(length) + ".txt"
    text_file = open(file_name, 'w')
    for word in bible_words:
        letters = list(word)
        word_length = len(letters) - 1
        if word_length == length:
            text_file.write(word)
    
    text_file.close()