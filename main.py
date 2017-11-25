import sys
import re

us_uk = []
for line in open('en_us_uk.txt', 'r').readlines():
    us_uk.append(line.split())
    
text = open(sys.argv[1], 'r').readlines()

splitter = re.compile(r'[ .,;:()*]', flags=re.IGNORECASE)
words = set()

for line in text:
    warr = splitter.split(line.strip().lower())
    warr = [s for s in warr if len(s) > 3]
    words |= set(warr)
print(words)
print(us_uk)
for word in words:
    if '-' in word:
        if word.replace('-', '') in words:
            print(f"Warning, using {word} and {word.replace('-', '')}") 

for us_word, uk_word in us_uk:
    if us_word in words and uk_word in words:
        print(f"Warning, both {us_word} and {uk_word} are used")
