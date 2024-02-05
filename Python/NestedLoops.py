#Nesting Loops

print('Nesting Loop Examples \n')

outer = ['outer1', 'outer2', 'outer3']
nest = ['nest1', 'nest2', 'nest3']

for x in outer:
    for y in nest:
        print(x, y)
    print('\n')

print('-----------------------------------')

numbers = [1,2,3]
letters = ['a','b','c']

for x in numbers:
    print(x)
    for y in letters:
        print(y)
    print('\n')

print('-----------------------------------')

car_type = ['Honda', 'Mazda', 'Volvo']
car_spec = ['5 Doors', '2 Bags Boot Space', 'SatNav', 'AirCon', '4 Wheels']

for car_model in car_type:
    print(car_model)
    for car_parts in car_spec:
        print(car_parts)
    print('\n')

print('------------------------------------')
