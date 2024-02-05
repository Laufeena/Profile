#formatting output
print("formatting outputs")
print('\n')

salary = 44000
txt = "You make {} dollars a year"
print(txt.format(salary))
print('\n')
print('------------------------------')

print("Multiple Curly Bracket")
print('\n')

string = "Dave loves {1} {3} and has {2} {0}."
print(string.format("kids", "cyber", 7, "security"))
print('\n')
print('----------------------------')

string = "Bob like to play {act} and eat {1} {0}."
print(string.format("dogs", "hot", act="games"))

print("Bob like to play {act} and eat {1} {0}.".format("dogs", "hot", act="games"))

print("-------------------------------")
