'''
You are given a set A and n other sets. 
Your job is to find whether set A is a strict superset of each of the N sets.
Print True, if A is a strict superset of each of the N sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

'''


A = set(map(int, input().split(' ')))
N = int(input())
check = list()
for _ in range(N):
    O = set(map(int, input().split(' ')))
    check.append(A.issuperset(O))
print(all(check))
