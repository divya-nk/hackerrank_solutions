'''
.update() or |= 
Update the set by adding elements from an iterable/another set.

.intersection_update() or &=
Update the set by keeping only the elements found in it and an iterable/another set.

.difference_update() or -=
Update the set by removing elements found in an iterable/another set.

.symmetric_difference_update() or ^=
Update the set by only keeping the elements found in either set, but not in both.

Task:
You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.
Your task is to execute those operations and print the sum of elements from set A.

'''

_, A = int(input()), set(map(int, input().split(' ')))
N = int(input())
for _ in range(N):
    command, o = input().split(' ')
    O = set(map(int, input().split(' ')))
    getattr(A, command)(O)    # getattr works like - A.command(O) - command here being the variable will be replaced by its valuable
print(sum(A))
