'''
You have a list of N  items together with their prices that consumers bought on a particular day. 
Your task is to print each item_name and net_price in order of its first occurrence.

Sample Input

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

Sample Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20

'''

from collections import OrderedDict
N = int(input())
odict = OrderedDict()

for _ in range(N):
    item, s, price = input().rpartition(' ')
    odict[item] = odict.get(item, 0) + int(price)

for item, price in odict.items():
    print(item, price)
