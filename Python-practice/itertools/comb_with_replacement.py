itertools.combinations_with_replacement(iterable, r) 
This tool returns r length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.


from itertools import combinations_with_replacement

s, r = input().split(' ')

t = list(combinations_with_replacement(sorted(s),int(r)))
for j in range(len(t)):
    print("".join(t[j]))
