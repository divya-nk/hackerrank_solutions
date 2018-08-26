'''
Sample Input
5 2   #length of word groups A and B respectively
a     # word group A starts
a
b
a
b
a   # word group B starts
b

Sample Output
1 2 4
3 5
Explanation
'a' appeared  times in positions 1,2  and 4. 
'b' appeared  times in positions 3 and 5. 
In the sample problem, if 'c' also appeared in word group B, you would print -1.
'''

from collections import defaultdict
d = defaultdict(list)   # this lets value as 'list' type 
n, m = map(int, input().split())

for i in range(1, n+1):
    d[input()].append(str(i))
for i in range(m):
    print(" ".join(d[input()] or -1))
