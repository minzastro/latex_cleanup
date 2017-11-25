import sys
import re

text = open(sys.argv[1], 'r').readlines()

splitter = re.compile(r'[ .,;:()*]', flags=re.IGNORECASE)
words = set()

for line in text:
	warr = splitter.split(line.lower())
	warr = [s for s in warr if len(s) > 3]
	words |= set(warr)
for word in words:
	if '-' in word:
		if word.replace('-', '') in words:
			print(f"Warning, using {word} and {word.replace('-', '')}") 


