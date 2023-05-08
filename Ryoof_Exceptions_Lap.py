# LAB_EXCEPTIONS


## Below you have a code that raises an exception , using what you learned do the following:
# - Find what type of exception is raised.
# - Hanlde the exception in try..except 
# - If operation successful , print "the operation is successful"
# - if operation fails, handle the specific exception that is raised , and print a relevant message.
'''****************************'''

# - Find what type of exception is raised ->>>> the type of exception is raised to : NameError

# - Hanlde the exception in try..except
def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)


b =None
while b is None:
    try:
        b=int(input("enter a number:"))
    except ValueError:
        print(f"You entered a wrong type of input, please fill it with integer value ")
    else:
        print("the operation is successful")

additoin(10, 20)



