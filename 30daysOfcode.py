# Day 8: Dictionaries and Maps
'''
Task 
Given 'n'  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each 'name' queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for 'name' is not found, print Not found instead.
'''

n = int(input())
phoneBook = dict(input().split() for _ in range(n))
while True:
    try:
        name = input()
        if name in phoneBook:
            print('{}={}'.format(name,phoneBook[name]))
        else:
            print("Not found")
    except:
        break
#===================================================================================================================================
# Day 3: 
'''
Task 
Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.
'''

if __name__ == '__main__':
    N = int(input())
    if N%2 == 0:
        if N>=2 and N<=5:
            print("Not Weird")
        elif N>=6 and N<=20:
            print("Weird")
        elif N>=20:
            print("Not Weird")
    else:
        print("Weird")
#===================================================================================================================================
# Day 2: 
'''
Task 
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.
Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!
'''

def solve(meal_cost, tip_percent, tax_percent):
    totalCost = round(meal_cost + meal_cost*tip_percent/100 + meal_cost*tax_percent/100)
    print("The total meal cost is {} dollars.".format(totalCost))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)

#===================================================================================================================================
# Day 1: Data Types

# Declare second integer, double, and String variables.
# Read and save an integer, double, and String to your variables.
secondInt = int(input())
secondDouble = float(input())
secondStr = str(input())
# Print the sum of both integer variables on a new line.
print(i+secondInt)
# Print the sum of the double variables on a new line.
print(d+secondDouble)
# Concatenate and print the String variables on a new line
print(s+secondStr)
# The 's' variable above should be printed first.
