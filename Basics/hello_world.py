#
## This code is just to remember basic concepts of python
###
# This is a simple 'hello world' program
#

##Def is  used to define a function
def main():
    print("Hello World!\n")
    name = input("What is your name? ")
    print("Hello, " + name + "!\n")
    print("Howdy \t", name, "\n") #This is another way of appending the variables


## Phython does not recongnize the main function by default
# Hence we need to tell the code to look for a function called main
# and run it

if __name__ == "__main__":
    main() 

