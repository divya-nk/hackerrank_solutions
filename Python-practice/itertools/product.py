'''
itertools.product()

This tool computes the cartesian product of input iterables. 
It is equivalent to nested for-loops. 
For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
'''

import itertools
def cartesian(A,B):
    prod = itertools.product(A,B)
    return list(prod)

A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))
print(*cartesian(A,B)) # to print unpacked list
