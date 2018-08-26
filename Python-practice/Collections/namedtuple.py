'''
collections.namedtuple()
Basically, namedtuples are easy to create, lightweight object types. 
They turn tuples into convenient containers for simple tasks. 
With namedtuples, you don’t have to use integer indices for accessing members of a tuple.

Example

Code 01

>>> from collections import namedtuple
>>> Point = namedtuple('Point','x,y')
>>> pt1 = Point(1,2)
>>> pt2 = Point(3,4)
>>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
>>> print dot_product
11
'''

from collections import namedtuple
N = int(input())
fields = input().split()
students = namedtuple('students', fields)
total = 0
for _ in range(N):
    stu = students(*input().split())
    total += int(stu.MARKS)
print('{:.2f}'.format(total/N))
