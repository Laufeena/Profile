#Default arguments

def student(firstname, lastname ="Bigger", major ="Information Technology"):
    print(firstname, lastname, "majors in", major)

student("Tony")
print('---------------------------------------------')
print('\n')
student("Tony", "Stark", "Physics")
print('---------------------------------------------')
print('\n')
student("Stan", "Lee")
print('---------------------------------------------')
