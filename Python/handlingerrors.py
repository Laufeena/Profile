#Handling exceptions

try:
    print(0/0)
except ZeroDivisionError:
    print ("You can't divide by zero!")

import sys

try:
    num = int(input("Enter a number between 1 - 10 "))
except ValueError:
    print("Please use numbers only")
    sys.exit()
print("You entered the number: ", num)

#try:
 #   data = something_that_can_go_wrong
#except IOError:
 #   handle_the_exception_error
#else:
 #   doing_different_exception_handling
#finally:
 #   print("Goodbye, World!")
