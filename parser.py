import math, json

def isnum(num):
	try:
		tmp = float(num)
		return True
	except:
		return False

def simple(word):
	global nouns
	for n in nouns:
		if word[:len(n)] == n:
			return n
	return word

# read text
with open('text2.txt', 'r', encoding='utf-8') as fp: pre_content = fp.read()

# load voca
with open('명사.txt', 'r', encoding='utf-8') as fp:
	nouns = fp.read().split()

# preprocess
content = []
for c in pre_content:
	if (ord('가') <= ord(c) <= ord('힣')) or (c in [' ', '.', '\n']): content.append(c)
content = ''.join(content)

# prepare database
word_cost = {}
word_count = {}

# split into sentences
lines = []
line = []
for word in content.split():
	# if sentence finished
	if word[-1] == '.':
		word = word[:-1]
		line.append(word)
		lines.append(' '.join(line))

		# update cost of words in the sentence
		for w in line:
			if simple(w) in word_cost: word_cost[simple(w)] += len(line) * line.count(w)
			else: word_cost[simple(w)] = len(line) * line.count(w)

		# prepare new line
		line = []
	else:
		line.append(word)

	# just count
	if simple(word) in word_count: word_count[simple(word)] += 1
	else: word_count[simple(word)] = 1

word_cost_sorted = sorted(word_cost, key=lambda x: word_cost[x], reverse=True)
word_count_sorted = sorted(word_count, key=lambda x: word_count[x], reverse=True)

print('========== word_cost ==========')
for w in word_cost_sorted[:20]:
	print('%s: %d' % (w, word_cost[w]))
print('========== word_count ==========')
for w in word_count_sorted[:20]:
	print('%s: %d' % (w, word_count[w]))
