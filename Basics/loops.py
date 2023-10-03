#here we will learn about loops in python

#lets define a while loop

x= 0

while (x < 5):
    print(x)
    x += 1

#lets define a for loop

for i in range(2,4): #remember that the last number is not included
    print("\n",i)

#we can also use for loops to iterate over a list and define i as the element of the list
# we can use the 'break' statement to break out of a loop, this can be used in combination with an if statement

while (x < 10):
    if (x == 7):
        break
    print("\t",x)
    x += 1

#the 'continue' command will skip the rest of the loop and continue with the next iteration. for example:

while (x < 10):
    x += 1
    if (x == 9):
        continue #-- this will result in a skip of the print statement below
    print("\t\t",x)