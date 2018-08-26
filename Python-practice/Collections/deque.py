'''
collections.deque()
A deque is a double-ended queue. It can be used to add or remove elements from both ends.

Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.
'''

from collections import deque
d = deque()
N = int(input())
for _ in range(N):
    inp = input().split()
    if (len(inp) == 1):
        getattr(d, inp[0])()
    else:
        getattr(d, inp[0])(inp[1])
print(* d)
