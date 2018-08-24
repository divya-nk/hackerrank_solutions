'''
You are given two sets, A and B. 
Your job is to find whether set A is a subset of set B.
'''

T = int(input())
subset = list()
for _ in range(T):
    _, A = int(input()), set(map(int, input().split(' ')))
    _, B = int(input()), set(map(int, input().split(' ')))
    subset.append(A.issubset(B))
print(*subset, sep = '\n')
        
