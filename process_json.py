
'''
Processes en_kjv.json into a text file containing a list of unique words.
en_kjv.json is from https://github.com/thiagobodruk/bible
'''

import json
import codecs
import string

with open("en_kjv.json") as handle:
    bible = json.load(codecs.open('en_kjv.json', 'r', 'utf-8-sig'))

bible_words = []

for book in bible:
    for verse in book['chapters']:
        for sentence in verse:
            clean_sentence = sentence.translate(str.maketrans('', '', string.punctuation))
            words = clean_sentence.split(' ')
            lower_words = [word.lower() for word in words]
            for word in lower_words:
                if not word in bible_words:
                    bible_words.append(word)
    
    print("Processed " + book['name'])

with open('bible_words.txt', 'w') as bible_words_file:
    for word in bible_words:
        bible_words_file.write('%s\n' % word)
