'''
Input Format

The first line contains an integer,n , the number of students who have subscribed to the English newspaper. 
The second line contains n space separated roll numbers of those students. 
The third line contains b, the number of students who have subscribed to the French newspaper. 
The fourth line contains b space separated roll numbers of those students.

Output the total number of students who have at least one subscription.
'''

E = int(input())
enews = set(map(int, input().split(' ')))
F = int(input())
fnews = set(map(int, input().split(' ')))
print(len(enews.union(fnews)))
