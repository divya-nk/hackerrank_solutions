'''
Input Format

The first line consists of an integer, K , the size of each group.
The second line contains the unordered elements of the room number list.

Task: 
'''

K = int(input())
roomlist = list(sorted(map(int, input().split(' '))))

for i in range(0, len(roomlist), K):
    if roomlist.count(roomlist[i]) == 1:
        print(roomlist[i])
    
# another approach

K = int(input())
roomlist = list(sorted(map(int, input().split(' '))))

captains_room = (sum(set(roomlist))*K - sum(roomlist))/(K-1)  #just do some algebra
print(int(captains_room))
