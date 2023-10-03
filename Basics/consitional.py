#here we will learn about conditional statements

##to practice lest just define a main function 

def main():
    global x,y
    x,y = 10,100

    if x > y :
        result = "x is greater than y"
    elif x == y:
        result = "x is equal to y"
    else:  
        result = "x is smaller than y"
    
    return print(result)

if __name__ == "__main__": #if there is a function called main, run it
    main()

#we can also use conditional statements in one line
result = x if (x>y) else y
print("\n",result)

##some new update to python is the match-case statement

variable = "three"
match variable:
        case "one":
            print("one")
        case "two":
            print("two")
        #we can also combine them 
        case "three" | "four":
            print("three or four")
        case _: #this is the default case
            print("default")