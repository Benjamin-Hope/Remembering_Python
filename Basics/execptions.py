
# Here we will learn exceptions:
# these are methods that can be used to handle errors in python

# example of an error:
# ---> x= 5/0 #this is a mathematical error
# the error is called ZeroDivisionError

# we can use try and except to handle this error:
try:
    x = 5/0
except:
    # if the try code failed it will print out this message, but can be substituted with more code and functions
    # if error the code JUMPS to the closest except block <-- this is important
    print("An error occured")


# we can also catch and create an exception for specific errors:

try:
    user = input("give me an error to divide 5 by: ")
    operation = 5/int(user)
    print(operation)
# since if we divide by zero it will give a ZeroDivisionError, we can catch this error and print out a message
except ZeroDivisionError as e:  # if we find this error, 'e' stands for _error_
    print("You can't divide by zero")
    # we can also have ValueError, which is when we did not provide a number
except ValueError as e:
    print("Please enter a number")
    print(e)  # this will print out the error message
finally:  # this section will run a code whenever we have an error or not
    print("this will run no matter what")
