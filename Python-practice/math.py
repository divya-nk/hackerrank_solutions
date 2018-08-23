#Power - mod Power

a = int(input())
b = int(input())
m = int(input())


print(pow(a,b)) # prints a^b
print(pow(a,b,m)) # prints a^b mod m (i.e) a^b % m

# Mod - Divmod

 # divmod, which takes two arguments a and b and 
 # returns a tuple containing the quotient of a/b  first and then the remainder.

print(a//b) #returns only the quotient
print(a%b) #returns only the remainder
print(divmod(a,b)) # returns tuple containing quotient and remainder
