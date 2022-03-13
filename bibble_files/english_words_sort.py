'''
Reads the text file ospd.txt and gets stats on the length of words in the dictionary (up to 8 letters long)
Then saves the words into separate lists based on the length of the word
'''

valid_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

with open('bibble_files/english/ospd.txt', 'r') as handle:
    english_words = handle.readlines()

print(len(english_words))

count = {}

for word in english_words:
    letters = list(word.lower())[:-1]

    valid = True
    for letter in letters:
        if not letter in valid_letters:
            valid = False

    if valid:
        length = len(letters)

        if not length in count:
            count[length] = 1
    
        else:
            count[length] += 1

sorted_count = {}

for i in sorted(count):
   sorted_count[i] = count[i]

print(sorted_count)

for length in sorted(count):
    file_name = "bibble_files/english/english_words_" + str(length) + ".txt"
    text_file = open(file_name, 'w')
    for word in english_words:
        letters = list(word.lower())[:-1]
        valid = True
        for letter in letters:
            if not letter in valid_letters:
                valid = False
        
        if valid:
            word_length = len(letters)
            if word_length == length:
                text_file.write(word)
    
    text_file.close()