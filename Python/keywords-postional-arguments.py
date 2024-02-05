#Keywords and positional arguments

def greet(name, msg = "How are you today?"):
    print("Hey", name + ", " + msg)

greet(name = "Dave", msg = "How do you do?")

print('----------------------------------')

greet(msg = "How do you do?", name = "Dave")

print('-----------------------------------')

greet("Dave", msg = "How do you do?")

print('-----------------------------------')

greet("Dave")
