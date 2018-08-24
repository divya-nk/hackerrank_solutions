# Set.add()

N = int(input())
stamps = set()
for _ in range(N):
    stamps.add(input())
print(len(stamps))

# Set .discard(), .remove() & .pop()

'''
Task
You have a non-empty set s, and you have to execute N commands given N in  lines.
The commands will be pop, remove and discard.

Input Format

The first line contains integer n, the number of elements in the set s. 
The second line contains n space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9. 
The third line contains integer N, the number of commands.
The next N lines contains either pop, remove and/or discard commands followed by their associated value.
'''

n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    command = input()
    if 'pop' in command:
        s.pop()         			# This operation removes and return an arbitrary element. If no elements to remove, raises KeyError.
    elif 'remove' in command:
        s.remove(int(command[7:]))	# remove(x), removes 'x'. raises KeyError if x not found. Returns None
    elif 'discard' in command:
        s.discard(int(command[7:]))	# discard(x), removes x. DOESN'T raise KeyError if x not found. Returns None.

print(sum(s))
