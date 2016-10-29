import sys

if len(sys.argv) != 2: sys.exit()

with open(sys.argv[1], 'r', encoding='utf-8') as fp:
	words = fp.read().split()

words_unique = set()

for w in words:
	words_unique.add(w)

words_unique = sorted(list(words_unique), reverse=True)

with open(sys.argv[1], 'w', encoding='utf-8') as fp:
	fp.write('\n'.join(words_unique))