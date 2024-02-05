#Reading Files
print('Reading Files')

#a = open("demo.txt", "r") - "r" is presumed if not put in!
#print(a.read())
#doesn't work if the document doesn't exist!

print('\n')
print('-------------------------------------')

print('\n')

a = open("Hello!.txt", "r")
print(a.read())

print('\n')
print('-----------------------------------')
print("Reading files - readline()")
print('\n')

a = open("Hello!.txt", "r")
print(a.readline())
a.close()

print('\n')
print('------------------------------')
print('\n')

a = open("Hello!.txt", "r")
print (a.read(3))
a.close

print('\n')
print('----------------------------------')
print('\n')
print ("Reading files - 'with'")

#reading files using "with" - autmatically closes the document being used.
with open ("Hello!.txt") as myfile:
    contents = myfile.read()
    print(contents)

a = open("Hello!.txt", "w")
a.write("What has happened now?")
a.close()

print('\n')
print('---------------------------------')

with open ("Hello!.txt") as myfile:
    contents = myfile.read()
    print(contents)
print('------------------------------------')

y = open("CreatedFile_1", "w")
y.close()
y = open("CreatedFile_1", "a")
y.write("I've Created this file using the 'x' code function" '\n')
y.write("I've also written to the created document using the 'a' function" '\n')
y.close()
y = open("CreatedFile_1", "r")
print(y.read())
y.close()

print('-------------------------------------------')

x = open("MyNewFile", "w")
x.close()

x = open("MyNewFile", "a")
b = 1
while b < 4:
    x.write("Here is line " + str(b) + '\n')
    b += 1
x.close()

x = open("MyNewFile", "r")
print(x.read())
x.close()

print('------------------------------------------------')
