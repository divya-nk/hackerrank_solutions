'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
'''



if __name__ == '__main__':
    N = int(input())
    x = list()
    for i in range(N):
        command = input()
        if 'insert' in command:
            _, i, e = command.split(' ')
            x.insert(int(i), int(e))
        elif 'print' in command:
            print(x)
        elif 'remove' in command:
            _, e = command.split(' ')
            x.remove(int(e))
        elif 'append' in command:
            _, e = command.split(' ')
            x.append(int(e))
        elif 'sort' in command:
            x = sorted(x)
        elif 'pop' in command:
            x.pop()
        elif 'reverse' in command:
            x = list(reversed(x))
