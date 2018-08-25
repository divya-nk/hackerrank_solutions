'''
You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.
'''

from collections import OrderedDict
N = int(input())
#words = [input() for _ in range(N)]
words = OrderedDict()
for _ in range(N):
    key = input()
    words[key] = words.get(key, 0) + 1
print(len(words))
print(* words.values())
