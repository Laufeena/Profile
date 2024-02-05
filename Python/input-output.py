#reading console inputs and formatting outputs
#input() for python 3.0 and above, raw_input() for python 2.0 generation.

txt = input("Can you see this? Yes or No ")
print("You said", txt)
print('/n')

#input with numbers
print("Input with Numbers"'/n')

txt = input("Give me a number: ")
num = int(txt)
print("The number you gave is: ", num)
print('/n')

txt = int(input("Give me a number: "))
print("The number you gave is: ", num)
print('/n')

#trying for errors
txt = input("Give me a number please: ")

try:
    num = int(txt)
    print("The number you gave is: ", num)
except ValueError:
    print("Please put in a real number, not a string or text")
print('/n')
