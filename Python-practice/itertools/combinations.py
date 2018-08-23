'''
itertools.combinations(iterable, r) 
This tool returns the r length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

Task: Same as permutations, except print combinations
'''

from itertools import combinations

s, r = input().split(' ')

for i in range(1, int(r)+1):
    t = list(combinations(sorted(s),i))
    for j in range(len(t)):
        print("".join(t[j]))
