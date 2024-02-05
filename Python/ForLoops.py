#FOR LOOPS
print('FOR loop examples')

colours = ['blue', 'red', 'pink', 'green']
for x in colours:
    print(x)

print('------------------------')

colours = ['blue', 'red', 'pink', 'green', 'yellow', 'white', 'black', 'orange']
for colour in colours:
    print(colour)

print('--------------------------')

#range (start, stop, step) start automatically at 0, stop has to be included, step increases or decreases, but step automatically increases by 1.

for a in range(10):
    print(a)

print('-----------------------------------')

for x in range (10,35):
    print(x)

print('-----------------------------------')

for y in range (0, 100, 2):
    print(y)

print('------------------------------------')

favfoods = ['peas', 'carrots', 'broccoli', 'wedges', 'chicken']
for foods in favfoods:
    print(foods)

print('-----------------------------------')

for odds in range (1, 30, 2):
    print(odds)

print('------------------------------------')
