'''
# Task:
Output the symmetric difference integers in ascending order, one per line.
The term symmetric difference indicates those values that exist in either m or n but do not exist in both.
'''

M = int(input())
m = set(map(int, input().split(' ')))
N = int(input())
n = set(map(int, input().split(' ')))

print(*sorted(m.symmetric_difference(n)), sep = '\n')

#print(*sorted(m.difference(n)), sep = '\n')
#print(*sorted(n.difference(m)), sep = '\n')


'''
Task 2:
Output the total number of students who are subscribed to the English newspaper only.
'''

_, enews = int(input()), set(map(int, input().split(' ')))
_, fnews = int(input()), set(map(int, input().split(' ')))

print(len(enews.difference(fnews)))
