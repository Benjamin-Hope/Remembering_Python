## Here we will address variables in Python

#There are 5 major data types in Python (Numbers, Strings, Lists, Tuples, Dictionaries)
# 1. int
# 2. float
# 3. bool
# 4. str
# 5. list
# 6. tuple --immutable list (cannot be changed)
# 7. dict

var_int = 10
var_float = 1.1
var_bool = True
var_str = "Rita is cool"
var_list = [0, 1 , "Ritussy", False]
var_tuple = ( 0, 1 ,2)
var_dic = {"one" : 1, "two" : 2}

#the command 'type()' is used to find the type of the variable

print("var_int is of type: ", type(var_int))
print("var_float is of type: ", type(var_float))
print("var_bool is of type: ", type(var_bool))
print("var_str is of type: ", type(var_str))
print("var_list is of type: ", type(var_list))
print("var_tuple is of type: ", type(var_tuple))
print("var_dic is of type: ", type(var_dic))

#lets access sequence types-- Python is zero-balanced 

print("\n Position 1 of a sequence type is :0, thus --> \t", var_list[0])

#we can also access slices:

print("\n",var_list[0:4]) # print stops in the last item, thus this is never printed
print("\n",var_list[0:4:2]) # we can also add a step index, here is 2 so prints every 2 steps

##sequences  an be reversed:
print("\n", var_list[::-1]) # only doing ':' wil show all the list, but setting a negative set ':-1' will reverse the list 

#to access dic you dont define it with the index number, but with the key.
print("\n", var_dic["one"])

##we cannot mix different types of variables, numbers and strings cannot mix, but float and int can

print("\n", str(var_int) + " dogs") # 'str' is used to convert to string

##We can define global variables, but we need to define them inside a function
## traditionally variables inside a function are local variables

def function():
    global x
    x = "Rita" ##alone this is a local variable and will not save outside the function
    print(x)

function() ## this will initialize the function and print the variable
print("\n",x) ## this will print the variable outside the function, because we defined it as global

#we can also delete variables with the command 'del'

del x ## this will delete the variable x