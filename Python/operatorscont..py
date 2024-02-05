#Bitwise Operators
print('Bitwise Operators')

a = 24
b = 60

print(bin(a))

print(bin(b))

print('Bitwise Operator - &')

a = 24
b = 60
print(a&b)

x = 223
y = 111
print(x&y)

print('-----------------------')

print('Bitwise Operator - |')

a = 24
b = 60
print(a|b)

x = 223
y = 111
print(x|y)

print('-----------------------')

print('Bitwise Operator - ^')

a = 24
b = 60
print(a^b)

x = 223
y = 111
print(x^y)

print('------------------------')

#Identity Operators
print('Identity Operator - is')

a = 2
b = 6
c = a

print(a is b)
print(a is c)

print('-----------------------')

print('Identity Operator - is not')

a = 2
b = 6
c = a

print(a is not b)
print(a is not c)

print('------------------------')

#Membership Operators
print('Membership Operators - in')

numbers = [1, 2, 3, 4]
print(2 in numbers)

colours = ['blue', 'red', 'yellow']
print('green' in colours)

print('-------------------------')

print('Membership Operators - not in')

numbers = [1, 2, 3, 4]
print(2 in numbers)

colours = ['blue', 'red', 'yellow']
print('green' in colours)

print('---------------------------')
