# TODO: here we will learn how to use functions in python

def func1():
    print("I am a function")

#lets create functions with arguments and return values

def func2(arg1, arg2):
    print(arg1, " ", arg2)
    y= arg1 + arg2
    return y

print(func2(3,2)) ## this will print the return value of the function

#lets define a function with default arguments values

def func3(a,b=1):
    y=1
    for i in range(b): #range of b= 1 ,thus for i is 1 to 1 
        y=y*a
    return y

print("\n",func3(3)) # this will print the return value of the function with the default value of b, since we did not defined it

#We can also have functions with undefined number of arguments

def und_func(*args):
    result = 0
    for x in args: ##this will do the loop for every argument in the function
        result = result + x
    return result

print("\n",und_func(1,2,3,4,5,6,7,8,9,10)) #this will print the sum of all the arguments 
